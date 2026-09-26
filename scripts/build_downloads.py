#!/usr/bin/env python3
"""Regenerate the download files from coumarins.json.

    pip install rdkit
    python3 scripts/build_downloads.py

coumarins.json is the source of truth. After editing it, run this script to
bring the other files in line:

  coumarinDB-SMILES.smi  rewritten from the JSON.
  coumarinDB-2D.sdf      SD properties rewritten from the JSON. The existing
                         2D coordinates are kept for every compound whose
                         structure has not changed. New compounds, or
                         compounds whose SMILES now describe a different
                         structure, get fresh 2D coordinates from RDKit.
  coumarinDB-3D.sdf      rebuilt from the SMILES: RDKit ETKDGv3 embedding with
                         a fixed random seed, then MMFF94s optimisation, all
                         hydrogens explicit. Stereocentres the SMILES leave
                         undefined get an arbitrary configuration.

Then run scripts/validate.py.
"""

import json
import re
import sys
from pathlib import Path

try:
    from rdkit import Chem, RDLogger
    from rdkit.Chem import AllChem
except ImportError:
    sys.exit("This script needs RDKit: pip install rdkit")

RDLogger.DisableLog("rdApp.*")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "coumarins.json"
SMILES_FILE = ROOT / "coumarinDB-SMILES.smi"
SDF_2D = ROOT / "coumarinDB-2D.sdf"
SDF_3D = ROOT / "coumarinDB-3D.sdf"

# SD property names used by both SDF files, in order, and the JSON field for each.
PROPERTIES = [
    ("Name", "name"),
    ("PubChem ID", "pubchem_id"),
    ("CDB ID", "cdb_id"),
    ("Smiles", "smiles"),
    ("Chemical class", "chemical_class"),
    ("Natural source", "natural_source"),
    ("Molecular Formula", "molecular_formula"),
    ("InChI-Key", "inchi_key"),
    ("Total Molweight", "total_molweight"),
    ("cLogP", "clogp"),
    ("cLogS", "clogs"),
    ("H-Acceptors", "h_acceptors"),
    ("H-Donors", "h_donors"),
    ("Rotatable Bonds", "rotatable_bonds"),
    ("Polar Surface Area", "polar_surface_area"),
]

SEED = 20230509
MMFF_MAX_ITERS = 2000


def connectivity(mol):
    """First block of the InChIKey: the skeleton, ignoring stereo and charge."""
    return Chem.MolToInchiKey(mol)[:14]


def write_smiles_file(rows):
    lines = ["Smiles\tCDB ID"] + [f"{r['smiles']}\t{r['cdb_id']}" for r in rows]
    SMILES_FILE.write_bytes(("\r\n".join(lines) + "\r\n").encode("utf-8"))


def existing_2d_blocks():
    """CDB ID -> molblock text (up to and including 'M  END') from the current 2D SDF."""
    blocks = {}
    if not SDF_2D.exists():
        return blocks
    text = SDF_2D.read_bytes().decode("utf-8")
    for record in re.split(r"^\$\$\$\$\r?\n", text, flags=re.M):
        molblock, sep, _ = record.partition("M  END\n")
        if sep:
            title = molblock.lstrip("\r\n").splitlines()[0].strip()
            blocks[title] = molblock + sep
    return blocks


def fresh_2d_block(row):
    mol = Chem.MolFromSmiles(row["smiles"])
    AllChem.Compute2DCoords(mol)
    mol.SetProp("_Name", row["cdb_id"])
    return Chem.MolToMolBlock(mol, forceV3000=True)


def write_2d(rows):
    blocks = existing_2d_blocks()
    out, redrawn = [], []
    for row in rows:
        block = blocks.get(row["cdb_id"])
        smiles_mol = Chem.MolFromSmiles(row["smiles"])
        keep = False
        if block is not None:
            old = Chem.MolFromMolBlock(block)
            keep = old is not None and connectivity(old) == connectivity(smiles_mol)
        if not keep:
            block = fresh_2d_block(row)
            redrawn.append(row["cdb_id"])
        props = "".join(f">  <{name}>\r\n{row[key]}\r\n\r\n" for name, key in PROPERTIES)
        out.append(block + props + "$$$$\r\n")
    SDF_2D.write_bytes("".join(out).encode("utf-8"))
    return redrawn


def embed_3d(smiles):
    mol = Chem.AddHs(Chem.MolFromSmiles(smiles))
    params = AllChem.ETKDGv3()
    params.randomSeed = SEED
    if AllChem.EmbedMolecule(mol, params) != 0:
        params.useRandomCoords = True
        if AllChem.EmbedMolecule(mol, params) != 0:
            return None, "embedding failed"
    props = AllChem.MMFFGetMoleculeProperties(mol, mmffVariant="MMFF94s")
    if props is None:
        AllChem.UFFOptimizeMolecule(mol, maxIters=MMFF_MAX_ITERS)
        return mol, "UFF (no MMFF parameters)"
    field = AllChem.MMFFGetMoleculeForceField(mol, props)
    if field.Minimize(maxIts=MMFF_MAX_ITERS) != 0:
        return mol, f"MMFF94s not converged after {MMFF_MAX_ITERS} steps"
    return mol, None


def write_3d(rows):
    notes = []
    writer = Chem.SDWriter(str(SDF_3D))
    for n, row in enumerate(rows, 1):
        mol, note = embed_3d(row["smiles"])
        if mol is None:
            writer.close()
            sys.exit(f"{row['cdb_id']}: could not generate 3D coordinates ({note})")
        if note:
            notes.append(f"{row['cdb_id']}: {note}")
        mol.SetProp("_Name", row["cdb_id"])
        for name, key in PROPERTIES:
            mol.SetProp(name, row[key])
        writer.write(mol)
        if n % 100 == 0:
            print(f"  3D: {n}/{len(rows)}", flush=True)
    writer.close()
    return notes


def main():
    rows = json.loads(DATA.read_text(encoding="utf-8"))
    bad = [r["cdb_id"] for r in rows if Chem.MolFromSmiles(r["smiles"]) is None]
    if bad:
        sys.exit(f"RDKit cannot parse the SMILES of: {', '.join(bad)}")

    write_smiles_file(rows)
    print(f"Wrote {SMILES_FILE.name}")

    redrawn = write_2d(rows)
    print(f"Wrote {SDF_2D.name}; new 2D coordinates for {len(redrawn)} compound(s)"
          + (f": {', '.join(redrawn)}" if redrawn else ""))

    notes = write_3d(rows)
    print(f"Wrote {SDF_3D.name}")
    for note in notes:
        print(f"  note: {note}")
    print("Now run: python3 scripts/validate.py")


if __name__ == "__main__":
    main()
