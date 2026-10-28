# Data model: Ticketing Tool Status: PACS Computerization, State A

## Tables

| Table | Grain | Description | Rows |
|---|---|---|---|
| `tickets_summary` | one row per metric | Ticket counters: raised, resolved, pending by level | 11 |
| `backlog_nov2025` | dimension x key | Open-ticket backlog on 6-Nov-2025, long format by dimension | 123 |
| `backlog_nov2025_side_age` | side x age band | Open tickets by owner and age band | 8 |
| `dev_tasks_summary` | dimension x key | Development task tracker, long format by dimension | 17 |
| `dev_tasks_timeline` | month | Development tasks started and completed per month | 10 |
| `taxonomy` | sub-nature | Ticket category taxonomy: nature, sub-nature, priority | 20 |
| `release_notes_status` | release item | Release 1.0.5.6 items with deployment status on 22-Dec-2025 and 12-Jan-2026 | 27 |
| `customizations_summary` | one row per status | Customization counts by status | 7 |
| `customizations_open` | customization | Open customization requests with age | 44 |
| `weekly_review_issues` | issue | Issues discussed in the 12-Sep-2024 weekly review | 11 |

## Columns

**tickets_summary**: `metric`, `value`, `group`

**backlog_nov2025**: `dimension`, `key`, `tickets`, `over_tat`, `avg_age`

**backlog_nov2025_side_age**: `side`, `age_band`, `tickets`

**dev_tasks_summary**: `dimension`, `key`, `tasks`, `avg_days_to_complete`

**dev_tasks_timeline**: `month`, `tasks_started`, `tasks_completed`

**taxonomy**: `nature`, `sub_nature`, `priority`

**release_notes_status**: `sno`, `item`, `status_dec`, `status_jan`, `bucket_dec`, `bucket_jan`

**customizations_summary**: `metric`, `value`

**customizations_open**: `cui`, `customization`, `assigned_to`, `start`, `age_days`

**weekly_review_issues**: `sno`, `issue`, `action_required`

## Relationships (create in Model view)

- `backlog_nov2025` and `backlog_nov2025_side_age` are independent fact tables (filter by `dimension` / `side`).
- `dev_tasks_summary[key]` is filtered together with `dimension`: always add a visual-level filter on `dimension`.
- All tables are small and unrelated; no relationships are required.
