# Data dictionary: Ticketing Tool Status: PACS Computerization, State A

Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.

## `tickets_summary`

Ticket counters: raised, resolved, pending by level. Grain: one row per metric. Rows: 11.

| Column | Type | Example |
|---|---|---|
| `metric` | str | Total Issue Raised |
| `value` | int64 | 50460 |
| `group` | str | Raised |

## `backlog_nov2025`

Open-ticket backlog on 6-Nov-2025, long format by dimension. Grain: dimension x key. Rows: 123.

| Column | Type | Example |
|---|---|---|
| `dimension` | str | side |
| `key` | str | With SI support |
| `tickets` | int64 | 51 |
| `over_tat` | int64 | 4 |
| `avg_age` | float64 | 1.16 |

## `backlog_nov2025_side_age`

Open tickets by owner and age band. Grain: side x age band. Rows: 8.

| Column | Type | Example |
|---|---|---|
| `side` | str | With SI support |
| `age_band` | str | 1-2 days |
| `tickets` | int64 | 30 |

## `dev_tasks_summary`

Development task tracker, long format by dimension. Grain: dimension x key. Rows: 17.

| Column | Type | Example |
|---|---|---|
| `dimension` | str | priority |
| `key` | str | P0 |
| `tasks` | int64 | 21 |
| `avg_days_to_complete` | float64 | 51.0 |

## `dev_tasks_timeline`

Development tasks started and completed per month. Grain: month. Rows: 10.

| Column | Type | Example |
|---|---|---|
| `month` | str | 2024-06 |
| `tasks_started` | int64 | 34 |
| `tasks_completed` | int64 | 0 |

## `taxonomy`

Ticket category taxonomy: nature, sub-nature, priority. Grain: sub-nature. Rows: 20.

| Column | Type | Example |
|---|---|---|
| `nature` | str | Technical |
| `sub_nature` | str | DCT - Customer Module |
| `priority` | str | High |

## `release_notes_status`

Release 1.0.5.6 items with deployment status on 22-Dec-2025 and 12-Jan-2026. Grain: release item. Rows: 27.

| Column | Type | Example |
|---|---|---|
| `sno` | str | 1 |
| `item` | str | Two Factor Authentication Implementation |
| `status_dec` | str | Not Deployed |
| `status_jan` | str | Not Deployed |
| `bucket_dec` | str | Not deployed |
| `bucket_jan` | str | Not deployed |

## `customizations_summary`

Customization counts by status. Grain: one row per status. Rows: 7.

| Column | Type | Example |
|---|---|---|
| `metric` | str | Total Customizations Requested |
| `value` | int64 | 57 |

## `customizations_open`

Open customization requests with age. Grain: customization. Rows: 44.

| Column | Type | Example |
|---|---|---|
| `cui` | str | MP0012 |
| `customization` | str | mobile app for pacs members  |
| `assigned_to` | str | Vendor |
| `start` | str | 2024-04-02 |
| `age_days` | int64 | 610 |

## `weekly_review_issues`

Issues discussed in the 12-Sep-2024 weekly review. Grain: issue. Rows: 11.

| Column | Type | Example |
|---|---|---|
| `sno` | int64 | 1 |
| `issue` | str |  The calculation of interest is still be |
| `action_required` | str | SI/district cooperative banks is request |
