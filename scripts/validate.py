#!/usr/bin/env python3
"""Check coumarins.json and the download files for consistency.

Run from anywhere:

    python3 scripts/validate.py

coumarins.json is the source of truth: the website reads it directly. This
script checks that every record is well formed, that the SMILES and SDF
downloads list the same compounds in the same order, that every SD property
matches the JSON, and that no structure has invalid or overlapping
coordinates. scripts/build_downloads.py regenerates the downloads from the JSON.

Errors (broken structure, mismatched files) make the script exit with status 1.
Warnings are curation notes, such as possible duplicates or empty fields.
They are printed but do not fail the run. Only the Python standard library is
used, so it runs anywhere, including GitHub Actions.
"""

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "coumarins.json"
SMILES_FILE = ROOT / "coumarinDB-SMILES.smi"
SDF_FILES = [ROOT / "coumarinDB-2D.sdf", ROOT / "coumarinDB-3D.sdf"]

# SD property name -> JSON field, as written by scripts/build_downloads.py.
SD_PROPERTIES = {
    "Name": "name", "PubChem ID": "pubchem_id", "CDB ID": "cdb_id", "Smiles": "smiles",
    "Chemical class": "chemical_class", "Natural source": "natural_source",
    "Molecular Formula": "molecular_formula", "InChI-Key": "inchi_key",
    "Total Molweight": "total_molweight", "cLogP": "clogp", "cLogS": "clogs",
    "H-Acceptors": "h_acceptors", "H-Donors": "h_donors",
    "Rotatable Bonds": "rotatable_bonds", "Polar Surface Area": "polar_surface_area",
}

FIELDS = [
    "name", "pubchem_id", "cdb_id", "molecular_formula", "smiles", "inchi_key",
    "chemical_class", "natural_source", "total_molweight", "clogp", "clogs",
    "h_acceptors", "h_donors", "rotatable_bonds", "polar_surface_area",
]
DECIMAL_FIELDS = ["total_molweight", "clogp", "clogs", "polar_surface_area"]
INTEGER_FIELDS = ["h_acceptors", "h_donors", "rotatable_bonds"]
REQUIRED = ["name", "cdb_id", "molecular_formula", "smiles", "inchi_key", "chemical_class"]

CDB_ID = re.compile(r"CDB\d{4}")
INCHI_KEY = re.compile(r"[A-Z]{14}-[A-Z]{10}-[A-Z]")
DECIMAL = re.compile(r"-?\d+(\.\d+)?")
INTEGER = re.compile(r"\d+")

MAX_LISTED = 10


def listing(items):
    items = list(items)
    shown = ", ".join(str(i) for i in items[:MAX_LISTED])
    return shown + (f", and {len(items) - MAX_LISTED} more" if len(items) > MAX_LISTED else "")


def check_records(rows, errors, warnings):
    if not isinstance(rows, list) or not rows:
        errors.append("coumarins.json must be a non-empty list of records")
        return []

    for n, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            errors.append(f"record {n} is not an object")
            continue
        where = row.get("cdb_id") or f"record {n}"
        missing = [f for f in FIELDS if f not in row]
        extra = [f for f in row if f not in FIELDS]
        if missing:
            errors.append(f"{where}: missing fields {missing}")
        if extra:
            errors.append(f"{where}: unexpected fields {extra}")
        for f in FIELDS:
            if f in row and not isinstance(row[f], str):
                errors.append(f"{where}: {f} should be a string, got {type(row[f]).__name__}")
        for f in REQUIRED:
            if not str(row.get(f, "")).strip():
                errors.append(f"{where}: {f} is empty")
        if row.get("cdb_id") and not CDB_ID.fullmatch(row["cdb_id"]):
            errors.append(f"{where}: CDB ID should look like CDB0001")
        if row.get("inchi_key") and not INCHI_KEY.fullmatch(row["inchi_key"]):
            errors.append(f"{where}: malformed InChIKey {row['inchi_key']!r}")
        if row.get("smiles") and re.search(r"\s", row["smiles"]):
            errors.append(f"{where}: SMILES contains whitespace")
        for f in DECIMAL_FIELDS:
            if not DECIMAL.fullmatch(str(row.get(f, "")).strip()):
                errors.append(f"{where}: {f} is not a number: {row.get(f)!r}")
        for f in INTEGER_FIELDS:
            if not INTEGER.fullmatch(str(row.get(f, "")).strip()):
                errors.append(f"{where}: {f} is not a whole number: {row.get(f)!r}")
        pubchem = str(row.get("pubchem_id", "")).strip()
        if pubchem and not pubchem.isdigit():
            errors.append(f"{where}: PubChem CID is not a number: {pubchem!r}")

    good = [r for r in rows if isinstance(r, dict)]
    ids = [r.get("cdb_id", "") for r in good]
    dup_ids = [i for i, c in collections.Counter(ids).items() if c > 1]
    if dup_ids:
        errors.append(f"duplicate CDB IDs: {listing(dup_ids)}")

    numbers = sorted(int(i[3:]) for i in ids if CDB_ID.fullmatch(i))
    if numbers:
        gaps = sorted(set(range(numbers[0], numbers[-1] + 1)) - set(numbers))
        if gaps:
            warnings.append(f"gaps in CDB ID numbering: {listing(f'CDB{g:04d}' for g in gaps)}")

    empty = collections.defaultdict(list)
    spacing = []
    for r in good:
        for f in ("pubchem_id", "natural_source"):
            if not str(r.get(f, "")).strip():
                empty[f].append(r.get("cdb_id"))
        for f in FIELDS:
            v = r.get(f)
            if isinstance(v, str) and v != " ".join(v.split()):
                spacing.append(f"{r.get('cdb_id')} ({f})")
    for f, where in empty.items():
        warnings.append(f"empty {f}: {listing(where)}")
    if spacing:
        warnings.append(f"leading, trailing or double spaces: {listing(spacing)}")

    for f, label in (("inchi_key", "InChIKey"), ("pubchem_id", "PubChem CID"), ("name", "name")):
        groups = collections.defaultdict(list)
        for r in good:
            v = str(r.get(f, "")).strip()
            if v:
                groups[v].append(r.get("cdb_id"))
        dups = [ids_ for ids_ in groups.values() if len(ids_) > 1]
        if dups:
            count = sum(len(d) for d in dups)
            warnings.append(
                f"{len(dups)} {label}s are shared by more than one record ({count} records), "
                f"possible duplicates: {listing('/'.join(d) for d in dups)}"
            )
    return ids


def read_smiles_file(errors):
    if not SMILES_FILE.exists():
        errors.append(f"{SMILES_FILE.name} is missing")
        return None
    pairs = []
    for n, line in enumerate(SMILES_FILE.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        parts = line.split()
        if n == 1 and parts[0].lower() == "smiles":
            continue  # header line
        if len(parts) < 2:
            errors.append(f"{SMILES_FILE.name} line {n}: expected SMILES and CDB ID")
            continue
        pairs.append((parts[0], parts[1]))
    return pairs


def sdf_records(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    return [r for r in re.split(r"^\$\$\$\$[ \t]*\r?$\n?", text, flags=re.M) if r.strip()]


def sdf_coordinates(record):
    """Atom coordinate strings of a V2000 or V3000 molblock, or None if unreadable."""
    lines = record.lstrip("\r\n").splitlines()
    try:
        if "V3000" in lines[3]:
            start = lines.index("M  V30 BEGIN ATOM") + 1
            end = lines.index("M  V30 END ATOM")
            return [tuple(line.split()[4:7]) for line in lines[start:end]]
        n_atoms = int(lines[3][:3])
        return [tuple(line.split()[:3]) for line in lines[4:4 + n_atoms]]
    except (IndexError, ValueError):
        return None


def sdf_properties(record):
    """SD property name -> value (multi-line values joined with newlines)."""
    _, _, data = record.partition("M  END")
    props = {}
    for block in re.split(r"\r?\n\s*\r?\n", data):
        lines = block.strip("\r\n").splitlines()
        if lines and lines[0].startswith(">"):
            m = re.match(r">.*?<([^>]+)>", lines[0])
            if m:
                props[m.group(1)] = "\n".join(line.rstrip("\r") for line in lines[1:])
    return props


def check_downloads(rows, ids, errors, warnings):
    by_id = {r.get("cdb_id"): r for r in rows if isinstance(r, dict)}

    pairs = read_smiles_file(errors)
    if pairs is not None:
        smi_ids = [i for _, i in pairs]
        if smi_ids != ids:
            only_json = sorted(set(ids) - set(smi_ids))
            only_smi = sorted(set(smi_ids) - set(ids))
            detail = []
            if only_json:
                detail.append(f"missing from the file: {listing(only_json)}")
            if only_smi:
                detail.append(f"not in coumarins.json: {listing(only_smi)}")
            if not detail:
                detail.append("same compounds, different order")
            errors.append(f"{SMILES_FILE.name} does not match coumarins.json ({'; '.join(detail)})")
        mismatched = [i for s, i in pairs if i in by_id and by_id[i].get("smiles") != s]
        if mismatched:
            errors.append(f"{SMILES_FILE.name}: SMILES differ from coumarins.json for {listing(mismatched)}")

    for path in SDF_FILES:
        if not path.exists():
            errors.append(f"{path.name} is missing")
            continue
        records = sdf_records(path)
        titles = [r.lstrip("\r\n").splitlines()[0].strip() for r in records]
        if titles != ids:
            first = next(
                (k for k, (t, i) in enumerate(zip(titles, ids)) if t != i),
                min(len(titles), len(ids)),
            )
            found = titles[first] if first < len(titles) else "end of file"
            expected = ids[first] if first < len(ids) else "no more records"
            errors.append(
                f"{path.name}: record titles do not match coumarins.json "
                f"({len(titles)} records vs {len(ids)}; first difference at record {first + 1}: "
                f"found {found}, expected {expected})"
            )
        unreadable, nan, overlapping, prop_diffs = [], [], [], []
        for title, rec in zip(titles, records):
            coords = sdf_coordinates(rec)
            if not coords:
                unreadable.append(title)
                continue
            if any("nan" in value.lower() for xyz in coords for value in xyz):
                nan.append(title)
            elif len(set(coords)) < len(coords):
                overlapping.append(title)
            row = by_id.get(title)
            if row:
                props = sdf_properties(rec)
                for name, key in SD_PROPERTIES.items():
                    if props.get(name) != row.get(key):
                        prop_diffs.append(f"{title} ({name})")
        if unreadable:
            errors.append(f"{path.name}: cannot read the atom block of {listing(unreadable)}")
        if nan:
            errors.append(f"{path.name}: {len(nan)} records have invalid coordinates (NaN): {listing(nan)}")
        if overlapping:
            errors.append(f"{path.name}: atoms share identical coordinates in {listing(overlapping)}")
        if prop_diffs:
            errors.append(
                f"{path.name}: {len(prop_diffs)} SD properties differ from coumarins.json "
                f"(run scripts/build_downloads.py): {listing(prop_diffs)}"
            )


def check_structures(rows, warnings):
    """Optional: with RDKit installed, check each SMILES against its stored InChIKey."""
    try:
        from rdkit import Chem, RDLogger
    except ImportError:
        return False
    RDLogger.DisableLog("rdApp.*")
    unparsable, connectivity, stereo = [], [], []
    for r in rows:
        mol = Chem.MolFromSmiles(r.get("smiles", ""))
        if mol is None:
            unparsable.append(r.get("cdb_id"))
            continue
        key = Chem.MolToInchiKey(mol)
        stored = r.get("inchi_key", "")
        if key[:14] != stored[:14]:
            connectivity.append(r.get("cdb_id"))
        elif key != stored:
            stereo.append(r.get("cdb_id"))
    if unparsable:
        warnings.append(f"RDKit cannot parse the SMILES of {listing(unparsable)}")
    if connectivity:
        warnings.append(f"SMILES and InChIKey describe different structures: {listing(connectivity)}")
    if stereo:
        warnings.append(
            f"{len(stereo)} SMILES do not reproduce the stereochemistry in the stored InChIKey: {listing(stereo)}"
        )
    return True


def main():
    errors, warnings = [], []
    try:
        rows = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {DATA.name}: {exc}")
        return 1

    ids = check_records(rows, errors, warnings)
    if ids:
        check_downloads(rows, ids, errors, warnings)
    rdkit = check_structures([r for r in rows if isinstance(r, dict)], warnings)

    print(f"Checked {len(rows)} records in {DATA.name}."
          + ("" if rdkit else " (Install RDKit to also check SMILES against InChIKeys.)"))
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
