# Policy Briefing: Cooperative Services Sample

An anonymized sample briefing for policy and program leaders: scorecard, progress timeline, generalized actions, integrations, and comparisons between anonymized regions.

## Dashboards

| Page | What it answers |
|---|---|
| `docs/scorecard.html` | Sample scorecard: Illustrative position on cooperative-service rollout measures. |
| `docs/directions.html` | Sample directions tracker: Generalized sample actions and their recorded evidence. |
| `docs/integrations.html` | Integrations and enhancements: Portal integrations with their status, and the Concept Note enhancement requirements by theme and module. |
| `docs/state-comparison.html` | Region A and Region B: Comparable sample progress measures as a share of the anonymized population in scope. |
| `docs/milestones.html` | Milestones and deadlines: Review dates, letters and deadlines on one timeline, plus the daily and monthly records the e-PACS SOP requires. |

## Headline KPIs

| KPI | Value | Definition |
|---|---|---|
| e-PACS achieved | 99.16% | Share of PACS working in e-PACS mode (9-Feb-2026 sample) |
| ERP onboarding | 2,494 | PACS onboarded on the ERP |
| Audit and YEP FY2024-25 | 2,494 | PACS with audit and year-end completed for 2024-25 |
| Ticket resolution rate | 99.99% | Tickets resolved as share of tickets raised |
| Enhancements completed | 54.4% | Completed enhancement requests as share of requests raised |
| PACS identified for reorganisation | 504 | PACS identified for bifurcation or reorganisation |
| Integrations requested | 7 | Portal integrations requested from Vendor |
| Support centres | 49 | District-level support centres (plus the state command centre) |
| Directions tracked | 6 | Directions under review |

Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).

## Data sources

| Source file | Used for |
|---|---|
| Programme review decks (PowerPoint) | Scorecard, enhancements, support, reorganisation |
| Committee review deck | Integrations and customization status |
| State review decks | Dated e-PACS progress |
| Ticket counter workbook | Ticket counters |
| state-level banking partner letter and record of discussion | Progress at a date, national directions |
| State SOP letter | Deadlines and daily reporting rules |
| Neighbouring-state comparison deck | Comparison metrics |
| Requirement note (Excel) | Enhancement requirements |

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

- Scorecard values are transcribed from slides and then rescaled for this edition.
- Progress points use each source's own definition (completed, certificates, reported) and must not be read as one continuous series.
- The comparison state deck is undated, so metrics are matched by name, not by date.
- Customization counts differ between sources; the tracker is used.

## Documentation

- [KPI dictionary](docs-md/KPI_DICTIONARY.md)
- [Data dictionary](docs-md/DATA_DICTIONARY.md)
- [Methodology](docs-md/METHODOLOGY.md)
