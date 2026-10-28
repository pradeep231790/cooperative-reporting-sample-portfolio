# Data dictionary: Training Status: PACS Computerization, State A

Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.

## `feb2026_district`

District-wise training counts, Feb 2026 (contacts removed). Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `total_pacs` | int64 | 35 |
| `trainings` | int64 | 0 |
| `participants` | int64 | 0 |
| `managers` | int64 | 0 |
| `operators` | int64 | 0 |
| `master_trainers` | int64 | 0 |
| `auditors` | int64 | 0 |
| `others` | int64 | 0 |
| `online` | int64 | 0 |
| `offline` | int64 | 0 |
| `modules` | str | 0 |

## `refresher_district`

Refresher coverage 7-15 Feb 2026 by district. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district` | str | District 01 |
| `pacs` | int64 | 35 |
| `pacs_with_training_date` | int64 | 0 |
| `managers_listed` | int64 | 55 |
| `operators_listed` | int64 | 35 |

## `refresher_daily`

PACS with a refresher training date, per day. Grain: date. Rows: 15.

| Column | Type | Example |
|---|---|---|
| `date` | str | 2026-01-10 |
| `pacs_trained` | int64 | 21 |
| `in_feb2026` | bool | False |

## `monthly_2025`

Monthly training sessions and attendance, May-Oct 2025. Grain: month x audience. Rows: 8.

| Column | Type | Example |
|---|---|---|
| `month` | str | 2025-05 |
| `audience` | str | PACS staff |
| `districts_covered` | int64 | 29 |
| `sessions` | int64 | 22 |
| `attendance` | int64 | 1089 |
| `online` | int64 | 18 |
| `offline` | int64 | 3 |
| `hybrid` | int64 | 0 |

## `edaksh_2024`

e-Daksh training sessions 2024. Grain: district. Rows: 52.

| Column | Type | Example |
|---|---|---|
| `district cooperative bank` | str | district cooperative bank 54 |
| `district` | str | District 01 |
| `pacs_count` | int64 | 35 |
| `module` | str | ERP |
| `training_date` | str | 2024-03-01 |
| `attendees` | int64 | 32 |

## `evidence_by_district`

Photo, PDF and video evidence file counts per district folder. Grain: district folder. Rows: 47.

| Column | Type | Example |
|---|---|---|
| `folder` | str | Monthly sheets |
| `sheets` | int64 | 1 |
| `photos` | int64 | 0 |
| `attendance_pdf` | int64 | 0 |
| `other` | int64 | 0 |
| `video` | int64 | 0 |
| `is_district` | bool | False |
