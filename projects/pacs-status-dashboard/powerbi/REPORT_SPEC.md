# Report specification: PACS Status Dashboard: State A

Build one report page per section. Apply `theme.json` (View > Themes > Browse for themes).

## Page: Status: day-end and entry (Nov-2025)

How many PACS have a current day-end, how fast it moved between 29-Sep and 5-Nov, and how old the last entries are.

- **Card visuals (one per KPI)**: KPI cards: PACS with a current day-end (5-Nov-2025), Current day-end %, Gain since 29-Sep-2025, Average day-end lag (days), Entry older than 180 days (6-Nov)
- **Line chart**: PACS with a current day-end, by snapshot. Source: `dayend_snapshots`
- **100% stacked bar (one per group)**: Age of last entry and last day-end (6-Nov). Source: `gap_bands`
- **Clustered bar chart (sorted descending)**: Average day-end gap by group (days). Source: `gap_groups`
- **Clustered bar chart (sorted descending)**: Ten districts with the longest day-end gap. Source: `gap_district`
- **Table or matrix with conditional formatting**: District table. Source: `dayend_progress_district`

## Page: Working PACS and laggards (3-Dec-2025)

Which PACS are working on the ERP, which are laggards, and when each PACS last closed a day.

- **Card visuals (one per KPI)**: KPI cards: Working PACS (3-Dec-2025), Laggards: day-end on or before 31-Mar-2025, Not working PACS
- **Clustered bar chart (sorted descending)**: Lowest working-PACS % by district. Source: `working_status_3dec2025`
- **Clustered bar chart (sorted descending)**: PACS by month of last day-end (state). Source: `dayend_month_3dec2025_state`
- **Table or matrix with conditional formatting**: Working status and laggards by district. Source: `working_status_3dec2025`

## Page: District league and branches (Sep-2025)

District league from the 18-Sep-2025 ERP status, with the district cooperative bank-branch table for drill-down.

- **Card visuals (one per KPI)**: KPI cards: ERP go-live % (18-Sep-2025), Red PACS (health score < 40, 18-Sep-2025), Stale PACS (no entry >180 days)
- **100% stacked bar**: Age of last entry (18-Sep-2025). Source: `sep2025_bands`
- **Clustered bar chart (sorted descending)**: Districts with the most Red PACS. Source: `sep2025_district`
- **Table or matrix with conditional formatting**: District league. Source: `sep2025_district`
- **Table or matrix with conditional formatting**: district cooperative bank branch table. Source: `sep2025_branch`

## Page: Red Zone PACS (Nov-2025 list)

PACS on the Red Zone list for audit, by district, and why audit is pending. District totals only.

- **Card visuals (one per KPI)**: KPI cards: Red Zone PACS (Nov-2025 list), Districts on the list, With audit and YEP completed
- **Clustered bar chart (sorted descending)**: Red Zone PACS by district. Source: `redzone_district`
- **Clustered bar chart (sorted descending)**: Reason for audit pendency (grouped). Source: `redzone_reasons`
- **Table or matrix with conditional formatting**: District table. Source: `redzone_district`
