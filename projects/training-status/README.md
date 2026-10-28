# Training Status: PACS Computerization, State A

Training reach for PACS managers, operators, master trainers and auditors: monthly sessions in 2025, the Feb-2026 district round, refresher coverage and the 2024 e-Daksh baseline.

## Dashboards

| Page | What it answers |
|---|---|
| `docs/feb2026.html` | District training round (Feb-2026): Sessions, participants and role mix by district for the February 2026 round. Source: district training tracker. |
| `docs/refresher.html` | Refresher training coverage (7-15 Feb): How many PACS have a refresher training date in the plan, by district and by day. |
| `docs/monthly-2025.html` | Monthly trainings (May-Oct 2025): Sessions and attendance per month from the district trackers. Sep-Oct are tracked separately for managers and operators. |
| `docs/baseline-2024.html` | e-Daksh baseline (2024): The first training round before go-live: attendees by module, month and district. |
| `docs/evidence.html` | Training evidence by district: How many photos and attendance PDFs are filed per district: a documentation check, not a count of trainings. |

## Headline KPIs

| KPI | Value | Definition |
|---|---|---|
| Trainings in Feb-2026 round | 39 | Training sessions reported by districts for February 2026 |
| Participants in Feb-2026 round | 1,238 | People trained in the February 2026 round |
| Districts with a training (Feb-2026) | 27 | Districts reporting at least one session, of 52 |
| Average participants per session | 31.7 | Mean attendance per Feb-2026 session |
| Online share (Feb-2026) | 43.6% | Online sessions as share of online + offline |
| Refresher coverage (PACS with a training date) | 57.8% | PACS whose staff have a training date in the 7-15 Feb refresher plan |
| Sessions May-Oct 2025 | 148 | Sessions with attendance recorded in the monthly trackers |
| Attendance May-Oct 2025 | 4,222 | Total attendance recorded |
| e-Daksh attendees 2024 | 2,304 | Attendees in the Feb-Mar 2024 baseline round |

Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).

## Data sources

| Source file | Used for |
|---|---|
| District training tracker (Excel) | District round: sessions, participants, role mix |
| Refresher training plan (Excel) | Coverage by district and by day (counts only) |
| Monthly training trackers (Excel) | Monthly sessions and attendance |
| Baseline training list (Excel) | First training round |
| Training evidence archive | Count of evidence files per district folder |

## Run it

```bash
pip install -r requirements.txt
python src/build.py                 # rebuild site, Power BI kit and docs from data/processed/
```
Open `docs/index.html` in a browser. No server is needed.

## Power BI

See [powerbi/README.md](powerbi/README.md): data model, DAX measures, Power Query loader, theme and a page-by-page report specification.

## Privacy

This is an anonymised portfolio edition:

- Real district, branch and bank names (replaced by pseudonyms).
- Original source files, PACS-level extracts, names, contact details and credentials.
- Real counts: all counts are rescaled, so absolute numbers are illustrative.

## Assumptions

- Districts showing 0 trainings may not have reported yet.
- Refresher coverage counts a PACS as covered when any training date is filled; it does not measure attendance. Dates typed with day and month swapped are corrected only when the swap lands in the plan month.
- Monthly sessions are rows with attendance above zero; mode spellings are normalised.
- Evidence counts show documentation, not the number of trainings held.

## Documentation

- [KPI dictionary](docs-md/KPI_DICTIONARY.md)
- [Data dictionary](docs-md/DATA_DICTIONARY.md)
- [Methodology](docs-md/METHODOLOGY.md)
