# PACS Status Dashboard: State A

Operational status of all PACS on the e-PACS ERP: day-end currency, age of last entry, working and laggard PACS, the Sep-2025 district league and the Red Zone list.

## Dashboards

| Page | What it answers |
|---|---|
| `docs/status-nov2025.html` | Status: day-end and entry (Nov-2025): How many PACS have a current day-end, how fast it moved between 29-Sep and 5-Nov, and how old the last entries are. |
| `docs/working-dec2025.html` | Working PACS and laggards (3-Dec-2025): Which PACS are working on the ERP, which are laggards, and when each PACS last closed a day. |
| `docs/league-sep2025.html` | District league and branches (Sep-2025): District league from the 18-Sep-2025 ERP status, with the district cooperative bank-branch table for drill-down. |
| `docs/redzone.html` | Red Zone PACS (Nov-2025 list): PACS on the Red Zone list for audit, by district, and why audit is pending. District totals only. |

## Headline KPIs

| KPI | Value | Definition |
|---|---|---|
| PACS with a current day-end (5-Nov-2025) | 1,851 | PACS whose last day-end is on or after 31-Mar-2025 |
| Current day-end % | 74.2% | Share of all PACS with a current day-end |
| Gain since 29-Sep-2025 | 952 | Increase in current-day-end PACS from the first to the last snapshot |
| Average day-end lag (days) | 235.6 | Mean days between the snapshot date and each PACS's last day-end |
| Entry older than 180 days (6-Nov) | 48.2% | PACS whose last entry is more than 180 days old |
| Working PACS (3-Dec-2025) | 54.1% | PACS working on the ERP as reported in the 4-Dec review |
| Laggards: day-end on or before 31-Mar-2025 | 1,058 | PACS whose last day-end is 31-Mar-2025 or earlier (3-Dec) |
| ERP go-live % (18-Sep-2025) | 99.0% | PACS live on the ERP |
| Red PACS (health score < 40, 18-Sep-2025) | 1,736 | PACS with an analyst health score below 40 |
| Red Zone PACS (Nov-2025 list) | 337 | PACS on the Red Zone list for audit |

Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).

## Data sources

| Source file | Used for |
|---|---|
| Operational status extracts (Excel) | Day-end snapshots, entry and day-end gaps, district and branch KPI tables |
| Review-meeting decks (PowerPoint) | Working PACS, laggards, month of last day-end |
| Audit Red Zone list (Excel) | Red Zone counts and audit-pendency reasons, aggregated |

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

- Current day-end: last day-end on or after 31-Mar-2025.
- Health score (0-100): go-live 25, day-end current 25, entry freshness 25, audit 10, YEP 5, HOC 5, T14 5. Weights are an analyst assumption; Red is below 40.
- Group names are as classified in the source trackers.
- Red Zone reasons are grouped by keyword from free text and are approximate.

## Documentation

- [KPI dictionary](docs-md/KPI_DICTIONARY.md)
- [Data dictionary](docs-md/DATA_DICTIONARY.md)
- [Methodology](docs-md/METHODOLOGY.md)
