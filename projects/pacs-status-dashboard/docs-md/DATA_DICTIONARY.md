# Data dictionary: PACS Status Dashboard: State A

Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.

## `dayend_snapshots`

State counts of current-day-end PACS at 10 snapshot dates. Grain: snapshot date. Rows: 10.

| Column | Type | Example |
|---|---|---|
| `date` | str | 2025-09-29 |
| `current` | int64 | 899 |
| `within_30d` | int64 | 165 |
| `avg_gap_days` | float64 | 357.8 |
| `total` | int64 | 2495 |
| `current_Grp1` | int64 | 899 |
| `current_Grp2` | int64 | 0 |
| `current_Grp3` | int64 | 0 |

## `dayend_progress_district`

District day-end currency, first vs last snapshot. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total` | int64 | 35 |
| `current` | int64 | 25 |
| `current_first` | int64 | 13 |
| `avg_gap` | float64 | 250.0 |
| `gain` | int64 | 13 |

## `gap_district`

Average entry and day-end gap by district, 6-Nov-2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total` | int64 | 35 |
| `avg_entry_gap` | float64 | 131.1 |
| `avg_dayend_gap` | float64 | 251.2 |
| `pct_entry_over_180` | float64 | 43.6 |

## `gap_bands`

PACS by age band of last entry and last day-end. Grain: measure x band. Rows: 10.

| Column | Type | Example |
|---|---|---|
| `measure` | str | Entry gap |
| `band` | str | 0-30 days |
| `pacs` | int64 | 612 |

## `gap_groups`

Average gaps by PACS group. Grain: group. Rows: 3.

| Column | Type | Example |
|---|---|---|
| `group` | str | Grp1 |
| `pacs` | int64 | 2407 |
| `avg_entry_gap` | float64 | 135.0 |
| `avg_dayend_gap` | float64 | 225.0 |

## `sep2025_district`

District KPI table, 18-Sep-2025 ERP entry status. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `dct_done` | int64 | 35 |
| `golive` | int64 | 35 |
| `dayend_current` | int64 | 6 |
| `entries_30d` | int64 | 1 |
| `stale_180d` | int64 | 11 |
| `audit_fy25` | int64 | 6 |
| `yep_fy25` | int64 | 6 |
| `hoc` | int64 | 1 |
| `red` | int64 | 28 |
| `avg_health` | float64 | 40.3 |

## `sep2025_branch`

district cooperative bank branch KPI table, 18-Sep-2025. Grain: branch. Rows: 701.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `district cooperative bank` | str | district cooperative bank 57 |
| `branch` | str | Branch 263 |
| `total_pacs` | int64 | 8 |
| `dct_done` | int64 | 8 |
| `golive` | int64 | 8 |
| `dayend_current` | int64 | 1 |
| `entries_30d` | int64 | 0 |
| `stale_180d` | int64 | 3 |
| `audit_fy25` | int64 | 1 |
| `yep_fy25` | int64 | 1 |
| `hoc` | int64 | 0 |
| `red` | int64 | 7 |
| `avg_health` | float64 | 39.0 |

## `sep2025_bands`

Entry freshness bands, 18-Sep-2025. Grain: band. Rows: 4.

| Column | Type | Example |
|---|---|---|
| `band` | str | Real-time (<=7d) |
| `pacs` | int64 | 128 |

## `working_status_3dec2025`

Working vs not working PACS by district, 3-Dec-2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 31 |
| `total_pacs` | int64 | 61 |
| `working` | int64 | 59 |
| `not_working` | int64 | 2 |
| `working_pct` | float64 | 96.7 |

## `laggards_3dec2025`

Laggard PACS (entry and day-end on or before 31-Mar-2025) by district. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `entry_on_or_before_31mar2025` | int64 | 3 |
| `dayend_on_or_before_31mar2025` | int64 | 12 |

## `dayend_month_3dec2025_district`

Month of last day-end by district, as on 3-Dec-2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `dayend_2024` | int64 | 1 |
| `m01` | float64 | 0.0 |
| `m02` | float64 | 0.0 |
| `m03` | float64 | 17.0 |
| `m04` | float64 | 16.0 |
| `m05` | float64 | 2.0 |
| `m06` | float64 | 1.0 |
| `m07` | float64 | 1.0 |
| `m08` | float64 | 0.0 |
| `m09` | float64 | 0.0 |
| `m10` | float64 | 5.0 |
| `m11` | float64 | 0.0 |
| `m12` | float64 | 11.0 |
| `dayend_2025` | int64 | 34 |

## `dayend_month_3dec2025_state`

State count of PACS by month of last day-end. Grain: month. Rows: 13.

| Column | Type | Example |
|---|---|---|
| `period` | str | 2024 (all months) |
| `pacs` | int64 | 149 |

## `redzone_district`

Red Zone PACS by district. Grain: district. Rows: 7.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 35 |
| `red_zone_pacs` | int64 | 56 |
| `yep_completed` | int64 | 22 |
| `ready_audit_25mar` | int64 | 45 |
| `ready_audit_30mar` | int64 | 43 |
| `avg_vouchers` | float64 | 2554.0 |

## `redzone_reasons`

Red Zone audit-pendency reasons, grouped. Grain: reason. Rows: 3.

| Column | Type | Example |
|---|---|---|
| `reason` | str | Audit and YEP completed |
| `pacs` | int64 | 144 |
