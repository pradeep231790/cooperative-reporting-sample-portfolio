# Data model: State VC Reporting: PACS Computerization, State A

## Tables

| Table | Grain | Description | Rows |
|---|---|---|---|
| `audit_progress_district` | district | Audit completed by district on 14-Nov, 20-Nov, 26-Nov, 3-Dec and 18-Dec 2025 | 52 |
| `epacs_progress_district` | district | e-PACS completed and certificates by district | 52 |
| `epacs_targets_dec2025` | district | Dated e-PACS targets by district, Nov-Dec 2025 | 52 |
| `state_timeline` | measure x source x date | State totals per measure, source deck and date | 10 |
| `weekly_audit_target_6nov` | district | Audit weekly target and achievement, 6-Nov-2025 | 52 |
| `weekly_epacs_target_6nov` | district | e-PACS weekly target and achievement, 6-Nov-2025 | 52 |
| `cert_pending_district_25jan2026` | district | PACS awaiting e-PACS certificate, by district, 25-Jan-2026 | 18 |
| `cert_expected_dates_25jan2026` | date | Expected certificate dates (count of PACS per date) | 6 |

## Columns

**audit_progress_district**: `district`, `total_pacs`, `audit_20nov`, `audit_26nov`, `audit_3dec`, `total_pacs_dec18`, `audit_14nov`, `audit_18dec`, `audit_remaining_18dec`

**epacs_progress_district**: `district`, `total_pacs`, `epacs_20nov`, `epacs_26nov`, `epacs_3dec`, `cert_14nov`, `entry_dayend_14nov`, `cert_18dec`, `entry_dayend_18dec`

**epacs_targets_dec2025**: `district`, `total_pacs`, `t_27nov`, `t_4dec`, `t_11dec`, `t_15dec`

**state_timeline**: `measure`, `source`, `date`, `value`, `total_pacs`

**weekly_audit_target_6nov**: `district`, `total`, `audit_30oct`, `system_audit_yep`, `manual_audit`, `total_audit`, `remaining`, `pct_done`, `w1_target`, `w1_ach`, `w1_extra`

**weekly_epacs_target_6nov**: `district`, `total`, `t_30nov`, `t_25nov`, `t_20nov`, `t_15nov`, `w1_target`, `certified`, `w1_ach`, `w1_extra`, `pct_t1`, `w2_target`, `w2_ach`, `w3_target`, `w3_ach`, `w4_target`, `w4_ach`

**cert_pending_district_25jan2026**: `district`, `pacs_listed`, `certificate_received`, `no_expected_date`, `certificate_pending`

**cert_expected_dates_25jan2026**: `expected`, `pacs`

## Relationships (create in Model view)

- Join `audit_progress_district[district]`, `epacs_progress_district[district]`, `epacs_targets_dec2025[district]`, `weekly_*[district]` and `cert_pending_district_25jan2026[district]` to a `dim_district` table (distinct district names) on district; use dim_district for slicers.
- `state_timeline` is standalone: filter on `measure` and plot `value` by `date`, with `source` as legend (definitions differ between decks).
