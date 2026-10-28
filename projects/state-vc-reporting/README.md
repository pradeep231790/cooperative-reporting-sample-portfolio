# State VC Reporting: PACS Computerization, State A

The weekly video-conference review pack for the State: audit and year-end progress, e-PACS completion and certification, dated targets, and certification-pending PACS, by district.

## Dashboards

| Page | What it answers |
|---|---|
| `docs/audit.html` | Audit and YEP progress: State and district audit completion across the 20-Nov to 18-Dec review dates. |
| `docs/epacs.html` | e-PACS completion and certification: e-PACS completed (4-Dec deck) and certificates issued (18-Dec deck) by district, with the dated Dec-2025 targets. |
| `docs/weekly-targets.html` | Weekly targets (6-Nov-2025): The week-1 plan for audit and e-PACS by district and how much was achieved. |
| `docs/cert-pending.html` | Certification pending (25-Jan-2026): PACS still waiting for their e-PACS certificate on 25-Jan-2026, with expected dates. District totals only. |
| `docs/slide-pack.html` | VC slide pack: formats and KPIs: The standard slides used in the weekly State VC, the KPI each slide carries and the dashboard page that reproduces it. |

## Headline KPIs

| KPI | Value | Definition |
|---|---|---|
| Audit and YEP completed (3-Dec-2025) | 2,193 | PACS with audit completed on 3-Dec-2025 (4-Dec deck) |
| Audit completion (3-Dec-2025) | 90.2% | Audit completed as share of all PACS |
| Audit gain in two weeks | 202 | Increase in audit completed between 20-Nov and 3-Dec |
| Audit completion (18-Dec-2025) | 98.2% | Audit completed as share of all PACS (18-Dec deck, different base) |
| e-PACS completed (3-Dec-2025) | 533 | PACS with e-PACS completed on 3-Dec-2025 (4-Dec deck) |
| e-PACS certificates (18-Dec-2025) | 1,022 | Certificates issued up to 18-Dec-2025 (18-Dec deck) |
| e-PACS certificate growth | 573 | Certificates added between 14-Nov and 18-Dec-2025 |
| PACS pending e-PACS certificate (25-Jan-2026) | 64 | PACS on the pending list without a certificate |
| Week-1 e-PACS target achieved (6-Nov-2025) | 35.5% | Week-1 achievement against week-1 target |

Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).

## Data sources

| Source file | Used for |
|---|---|
| Weekly VC review decks (PowerPoint) | Audit and e-PACS comparisons, dated targets |
| Working presentation (PowerPoint) | Audit and certificates at two dates |
| Weekly target workbook (Excel) | Weekly audit and e-PACS targets and achievement |
| Certification-pending list (Excel) | Pending certificates by district, aggregated |

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

- Two review decks use different bases and definitions, so audit and e-PACS series are plotted per source and not merged.
- e-PACS completed and e-PACS certificates are different measures.
- Expected certificate dates are parsed from free text; unreadable dates are counted as no expected date.

## Documentation

- [KPI dictionary](docs-md/KPI_DICTIONARY.md)
- [Data dictionary](docs-md/DATA_DICTIONARY.md)
- [Methodology](docs-md/METHODOLOGY.md)
