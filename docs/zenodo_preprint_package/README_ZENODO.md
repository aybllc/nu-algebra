# Nominal/Uncertainty Algebra as a Peer Review Instrument in Psychological Science: A Conservative Framework for Claim Robustness

## What this is
A preprint package intended for direct upload to Zenodo as a *Publication → Preprint*. It includes:
- `zenodo.json`: Deposit metadata (edit author list/affiliations before upload)
- `preprint.md`: The manuscript text (APA-style sections)
- `nu_psych_audit_expanded.csv`: N/U audit table (6 case studies)
- `nu_psych_audit_expanded_su_ratio.png`: S/U ratio figure
- `CITATION.cff`: Citation metadata for GitHub and other services
- `LICENSE`: CC-BY-4.0

## How to publish on Zenodo (UI)
1. Log in to Zenodo → New Upload.
2. Drag the contents of this folder (or a zip of it) into the "Files" area.
3. Set **Upload type** = Publication → Preprint.
4. Paste the **Title** and **Abstract** from `preprint.md` (or rely on `zenodo.json` if using the API).
5. Fill **Authors** (order, affiliations, ORCIDs).
6. Set **License** = CC-BY-4.0 (or your preferred open license).
7. Add **Related identifiers** → type: DOI, relation: *isSupplementedBy* → `10.5281/zenodo.17221863`.
8. Click **Save** → **Publish** (Zenodo will mint a DOI).

## How to publish via API
- Create a Personal Access Token in Zenodo.
- POST `zenodo.json` (as `metadata`) + files to the depositions endpoint.
- Finally `POST /depositions/<built-in function id>/actions/publish` to mint the DOI.

## Notes
- Replace placeholders in `zenodo.json` and `CITATION.cff`.
- Convert `preprint.md` to PDF if your target community prefers PDFs (e.g., `pandoc preprint.md -o preprint.pdf`).

## Dataset link
N/U Numerical Validation Dataset (70k+ cases): DOI 10.5281/zenodo.17221863.
