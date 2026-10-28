# Methodology and assumptions: PACS Status Dashboard: State A

## Assumptions to review

- Current day-end: last day-end on or after 31-Mar-2025.
- Health score (0-100): go-live 25, day-end current 25, entry freshness 25, audit 10, YEP 5, HOC 5, T14 5. Weights are an analyst assumption; Red is below 40.
- Group names are as classified in the source trackers.
- Red Zone reasons are grouped by keyword from free text and are approximate.

## Data sources

| Source file | Used for |
|---|---|
| Operational status extracts (Excel) | Day-end snapshots, entry and day-end gaps, district and branch KPI tables |
| Review-meeting decks (PowerPoint) | Working PACS, laggards, month of last day-end |
| Audit Red Zone list (Excel) | Red Zone counts and audit-pendency reasons, aggregated |

## Deliberately excluded

- Real district, branch and bank names (replaced by pseudonyms).
- Original source files, PACS-level extracts, names, contact details and credentials.
- Real counts: all counts are rescaled, so absolute numbers are illustrative.
