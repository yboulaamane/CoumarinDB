# CoumarinDB

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yboulaamane/CoumarinDB/main/assets/brand/logo-dark.svg">
  <img src="assets/brand/logo.svg" alt="CoumarinDB" height="96">
</picture>

*A manually curated database containing chemical information for naturally occurring coumarins.*

Coumarin is considered a versatile and privileged scaffold in medicinal chemistry. In recent decades, a large number of natural products containing the coumarin scaffold have been isolated and identified from natural resources. The literature shows that coumarin derivatives display a wide spectrum of biological activities such as antibacterial, antioxidant, anticoagulant, anti-inflammatory and neuroprotective properties.

CoumarinDB collects chemical information about naturally occurring coumarins, to cope with the growing amount of available data and to speed up drug discovery from natural products.

**Browse it online:** https://yboulaamane.github.io/CoumarinDB/

## What the website does

- Search by name, CDB ID, PubChem CID, formula, SMILES, InChIKey or natural source
- Filter by chemical class, molecular weight, cLogP and TPSA, and by Lipinski's and Veber's rules
- Sort by any column and draw each 2D structure in the browser
- Open any compound for its full record, a PubChem link and copy buttons
- Export the filtered compounds as CSV or SMILES
- Share a filtered view or a compound: filters are kept in the URL, and `#CDB0001` opens that compound

## Files

| File | Contents |
|---|---|
| `coumarins.json` | The database. The website reads this file directly. |
| `coumarinDB-2D.sdf` | 2D structures with all fields as SD properties |
| `coumarinDB-3D.sdf` | 3D structures with all fields as SD properties |
| `coumarinDB-SMILES.smi` | Tab-separated SMILES and CDB ID, with a header line |
| `index.html`, `assets/` | The website |
| `scripts/validate.py` | Consistency checks for all of the above |
| `assets/brand/` | Logo (light and dark), icon and social preview image |

Each record in `coumarins.json` has these fields, all stored as text:

| Field | Meaning |
|---|---|
| `cdb_id` | CoumarinDB identifier, for example `CDB0001` |
| `name` | Compound name |
| `pubchem_id` | PubChem compound ID (CID) |
| `molecular_formula` | Molecular formula |
| `smiles` | SMILES |
| `inchi_key` | InChIKey |
| `chemical_class` | Structural class of the coumarin |
| `natural_source` | Natural source reported for the compound |
| `total_molweight` | Molecular weight (g/mol) |
| `clogp` | Calculated logP |
| `clogs` | Calculated log solubility |
| `h_acceptors`, `h_donors` | Hydrogen-bond acceptors and donors |
| `rotatable_bonds` | Rotatable bonds |
| `polar_surface_area` | Polar surface area (Å²) |

## How to cite

If you use CoumarinDB, please cite the related article:

> Chemical library design, QSAR modeling and molecular dynamics simulations of naturally occurring coumarins as dual inhibitors of MAO-B and AChE. *Journal of Biomolecular Structure and Dynamics*. https://doi.org/10.1080/07391102.2023.2209650

## Updating the data

1. Edit `coumarins.json`. There is no build step: the website picks up the change on the next page load.
2. Keep `coumarinDB-SMILES.smi` and both SDF files in step with it: same compounds, same order, same SMILES.
3. Run the checks:

   ```bash
   python3 scripts/validate.py
   ```

   Errors (malformed records, files out of step) exit with status 1. Warnings, such as possible duplicates or empty fields, are curation notes and do not fail the run. The same check runs on GitHub for every push and pull request.

To preview the website locally, serve the folder over HTTP (opening `index.html` straight from disk does not work, because browsers block it from reading `coumarins.json`):

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

2D structures are drawn with [SmilesDrawer](https://github.com/reymond-group/smilesDrawer) (MIT licence), loaded from the jsDelivr CDN. If the CDN is unreachable, the table still works without structures.

## References

1. Dean, F. M. (1952). Naturally occurring coumarins. *Fortschritte der Chemie Organischer Naturstoffe / Progress in the Chemistry of Organic Natural Products / Progrès dans la Chimie des Substances Organiques Naturelles*, 225–291.
2. Soine, T. O. (1964). Naturally occurring coumarins and related physiological activities. *Journal of Pharmaceutical Sciences*, 53(3), 231–264.
3. Murray, R. D. (2002). The naturally occurring coumarins. *Fortschritte der Chemie Organischer Naturstoffe / Progress in the Chemistry of Organic Natural Products*, 1–619.
4. Sarker, S. D., & Nahar, L. (2017). Progress in the chemistry of naturally occurring coumarins. *Progress in the Chemistry of Organic Natural Products*, 106, 241–304.
