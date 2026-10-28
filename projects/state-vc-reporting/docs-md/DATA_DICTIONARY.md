# Data dictionary: State VC Reporting: PACS Computerization, State A

Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.

## `audit_progress_district`

Audit completed by district on 14-Nov, 20-Nov, 26-Nov, 3-Dec and 18-Dec 2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `audit_20nov` | int64 | 27 |
| `audit_26nov` | int64 | 28 |
| `audit_3dec` | int64 | 31 |
| `total_pacs_dec18` | int64 | 35 |
| `audit_14nov` | int64 | 27 |
| `audit_18dec` | int64 | 34 |
| `audit_remaining_18dec` | int64 | 1 |

## `epacs_progress_district`

e-PACS completed and certificates by district. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `epacs_20nov` | int64 | 1 |
| `epacs_26nov` | int64 | 2 |
| `epacs_3dec` | int64 | 5 |
| `cert_14nov` | int64 | 2 |
| `entry_dayend_14nov` | int64 | 1 |
| `cert_18dec` | int64 | 9 |
| `entry_dayend_18dec` | int64 | 9 |

## `epacs_targets_dec2025`

Dated e-PACS targets by district, Nov-Dec 2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `t_27nov` | int64 | 6 |
| `t_4dec` | int64 | 11 |
| `t_11dec` | int64 | 16 |
| `t_15dec` | int64 | 3 |

## `state_timeline`

State totals per measure, source deck and date. Grain: measure x source x date. Rows: 10.

| Column | Type | Example |
|---|---|---|
| `measure` | str | Audit |
| `source` | str | 4-Dec deck |
| `date` | str | 2025-11-20 |
| `value` | int64 | 1991 |
| `total_pacs` | int64 | 2495 |

## `weekly_audit_target_6nov`

Audit weekly target and achievement, 6-Nov-2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 24 |
| `total` | int64 | 71 |
| `audit_30oct` | int64 | 71 |
| `system_audit_yep` | int64 | 71 |
| `manual_audit` | int64 | 0 |
| `total_audit` | int64 | 71 |
| `remaining` | int64 | 0 |
| `pct_done` | float64 | 100.0 |
| `w1_target` | float64 | 0.0 |
| `w1_ach` | int64 | 0 |
| `w1_extra` | float64 | 0.0 |

## `weekly_epacs_target_6nov`

e-PACS weekly target and achievement, 6-Nov-2025. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 28 |
| `total` | int64 | 54 |
| `t_30nov` | int64 | 25 |
| `t_25nov` | int64 | 8 |
| `t_20nov` | int64 | 1 |
| `t_15nov` | int64 | 19 |
| `w1_target` | float64 | 16.0 |
| `certified` | float64 | 2.0 |
| `w1_ach` | int64 | 0 |
| `w1_extra` | float64 | 16.0 |
| `pct_t1` | float64 | 0.0 |
| `w2_target` | float64 | 17.2 |
| `w2_ach` | float64 |  |
| `w3_target` | float64 | 11.0 |
| `w3_ach` | float64 |  |
| `w4_target` | float64 | 10.1 |
| `w4_ach` | float64 |  |

## `cert_pending_district_25jan2026`

PACS awaiting e-PACS certificate, by district, 25-Jan-2026. Grain: district. Rows: 18.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `pacs_listed` | int64 | 1 |
| `certificate_received` | int64 | 0 |
| `no_expected_date` | int64 | 0 |
| `certificate_pending` | int64 | 1 |

## `cert_expected_dates_25jan2026`

Expected certificate dates (count of PACS per date). Grain: date. Rows: 6.

| Column | Type | Example |
|---|---|---|
| `expected` | str | 2026-01-25 |
| `pacs` | int64 | 4 |
