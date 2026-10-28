# Data model: PACS Status Dashboard: State A

## Tables

| Table | Grain | Description | Rows |
|---|---|---|---|
| `dayend_snapshots` | snapshot date | State counts of current-day-end PACS at 10 snapshot dates | 10 |
| `dayend_progress_district` | district | District day-end currency, first vs last snapshot | 52 |
| `gap_district` | district | Average entry and day-end gap by district, 6-Nov-2025 | 52 |
| `gap_bands` | measure x band | PACS by age band of last entry and last day-end | 10 |
| `gap_groups` | group | Average gaps by PACS group | 3 |
| `sep2025_district` | district | District KPI table, 18-Sep-2025 ERP entry status | 52 |
| `sep2025_branch` | branch | district cooperative bank branch KPI table, 18-Sep-2025 | 701 |
| `sep2025_bands` | band | Entry freshness bands, 18-Sep-2025 | 4 |
| `working_status_3dec2025` | district | Working vs not working PACS by district, 3-Dec-2025 | 52 |
| `laggards_3dec2025` | district | Laggard PACS (entry and day-end on or before 31-Mar-2025) by district | 52 |
| `dayend_month_3dec2025_district` | district | Month of last day-end by district, as on 3-Dec-2025 | 52 |
| `dayend_month_3dec2025_state` | month | State count of PACS by month of last day-end | 13 |
| `redzone_district` | district | Red Zone PACS by district | 7 |
| `redzone_reasons` | reason | Red Zone audit-pendency reasons, grouped | 3 |

## Columns

**dayend_snapshots**: `date`, `current`, `within_30d`, `avg_gap_days`, `total`, `current_Grp1`, `current_Grp2`, `current_Grp3`

**dayend_progress_district**: `district`, `total`, `current`, `current_first`, `avg_gap`, `gain`

**gap_district**: `district`, `total`, `avg_entry_gap`, `avg_dayend_gap`, `pct_entry_over_180`

**gap_bands**: `measure`, `band`, `pacs`

**gap_groups**: `group`, `pacs`, `avg_entry_gap`, `avg_dayend_gap`

**sep2025_district**: `district`, `total_pacs`, `dct_done`, `golive`, `dayend_current`, `entries_30d`, `stale_180d`, `audit_fy25`, `yep_fy25`, `hoc`, `red`, `avg_health`

**sep2025_branch**: `district`, `district cooperative bank`, `branch`, `total_pacs`, `dct_done`, `golive`, `dayend_current`, `entries_30d`, `stale_180d`, `audit_fy25`, `yep_fy25`, `hoc`, `red`, `avg_health`

**sep2025_bands**: `band`, `pacs`

**working_status_3dec2025**: `district`, `total_pacs`, `working`, `not_working`, `working_pct`

**laggards_3dec2025**: `district`, `total_pacs`, `entry_on_or_before_31mar2025`, `dayend_on_or_before_31mar2025`

**dayend_month_3dec2025_district**: `district`, `dayend_2024`, `m01`, `m02`, `m03`, `m04`, `m05`, `m06`, `m07`, `m08`, `m09`, `m10`, `m11`, `m12`, `dayend_2025`

**dayend_month_3dec2025_state**: `period`, `pacs`

**redzone_district**: `district`, `red_zone_pacs`, `yep_completed`, `ready_audit_25mar`, `ready_audit_30mar`, `avg_vouchers`

**redzone_reasons**: `reason`, `pacs`

## Relationships (create in Model view)

- Create `dim_district` (distinct district names from all district tables) and relate each `district` column to it (many-to-one, single direction).
- `sep2025_branch[district]` also relates to `dim_district`.
- `dayend_snapshots`, `gap_bands`, `gap_groups`, `sep2025_bands`, `dayend_month_3dec2025_state` and `redzone_reasons` are standalone state-level tables.
