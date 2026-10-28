# Data model: Training Status: PACS Computerization, State A

## Tables

| Table | Grain | Description | Rows |
|---|---|---|---|
| `feb2026_district` | district | District-wise training counts, Feb 2026 (contacts removed) | 52 |
| `refresher_district` | district | Refresher coverage 7-15 Feb 2026 by district | 52 |
| `refresher_daily` | date | PACS with a refresher training date, per day | 15 |
| `monthly_2025` | month x audience | Monthly training sessions and attendance, May-Oct 2025 | 8 |
| `edaksh_2024` | district | e-Daksh training sessions 2024 | 52 |
| `evidence_by_district` | district folder | Photo, PDF and video evidence file counts per district folder | 47 |

## Columns

**feb2026_district**: `district`, `total_pacs`, `trainings`, `participants`, `managers`, `operators`, `master_trainers`, `auditors`, `others`, `online`, `offline`, `modules`

**refresher_district**: `district`, `pacs`, `pacs_with_training_date`, `managers_listed`, `operators_listed`

**refresher_daily**: `date`, `pacs_trained`, `in_feb2026`

**monthly_2025**: `month`, `audience`, `districts_covered`, `sessions`, `attendance`, `online`, `offline`, `hybrid`

**edaksh_2024**: `district cooperative bank`, `district`, `pacs_count`, `module`, `training_date`, `attendees`

**evidence_by_district**: `folder`, `sheets`, `photos`, `attendance_pdf`, `other`, `video`, `is_district`

## Relationships (create in Model view)

- `dim_district` is not required: join `feb2026_district[district]` to `refresher_district[district]` and `edaksh_2024[district]` on district name (many-to-one after de-duplication).
- `monthly_2025` and `refresher_daily` are standalone time tables (use month / date on the axis).
