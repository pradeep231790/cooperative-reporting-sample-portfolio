# Data dictionary: Policy Briefing: Cooperative Services Sample

Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.

## `statea_scorecard`

State scorecard metrics with date and source. Grain: metric. Rows: 20.

| Column | Type | Example |
|---|---|---|
| `metric` | str | PACS sanctioned |
| `value` | float64 | 2495.0 |
| `unit` | str | PACS |
| `as_of` | str | 2025-12-04 |
| `source` | str | national review sub-committee deck 4-Dec |

## `statea_progress_timeline`

e-PACS progress at dated points (definitions differ by source). Grain: date x measure. Rows: 6.

| Column | Type | Example |
|---|---|---|
| `date` | str | 2025-11-20 |
| `measure` | str | e-PACS completed (4-Dec deck definition) |
| `pacs` | int64 | 324 |
| `total_pacs` | int64 | 2495 |
| `source` | str | VC review deck 4-Dec-2025 |
| `group` | str | e-PACS completed (4-Dec deck) |
| `pct` | float64 | 13.0 |

## `milestones`

Review milestones and deadlines. Grain: event. Rows: 12.

| Column | Type | Example |
|---|---|---|
| `date` | str | 2025-11-06 |
| `event` | str | State VC: weekly targets set; first cert |
| `source` | str | VC Slide Target 06-11-2025 |

## `policy_directions`

policy briefing directions of 28-Jan-2026 with State A evidence. Grain: direction. Rows: 6.

| Column | Type | Example |
|---|---|---|
| `no` | int64 | 1 |
| `area` | str | Payments |
| `direction` | str | Standardise vendor payment mechanism; pe |
| `deadline` | str | Immediate |
| `owner` | str | policy briefing / cooperative registrar |
| `statea_evidence` | str | Outside this dashboard's scope |

## `integrations`

Portal integrations and status. Grain: integration. Rows: 9.

| Column | Type | Example |
|---|---|---|
| `integration` | str | State family-ID portal portal |
| `purpose` | str | Verify farmer identity, family details,  |
| `status` | str | Pending at Vendor (national review sub-c |

## `statea_vs_stateb`

State A vs State B progress, same metric. Grain: metric. Rows: 3.

| Column | Type | Example |
|---|---|---|
| `metric` | str | DCT done |
| `statea_pacs` | int64 | 2495 |
| `statea_total` | int64 | 2495 |
| `stateb_pacs` | int64 | 833 |
| `source` | str | State A 9-Feb-2026; State B deck |
| `stateb_total` | int64 | 980 |
| `statea_pct` | float64 | 100.0 |
| `stateb_pct` | float64 | 85.0 |

## `statea_vs_stateb_scale`

State A vs State B scale. Grain: metric. Rows: 2.

| Column | Type | Example |
|---|---|---|
| `metric` | str | Districts with support centres |
| `state_a` | float64 | 27.0 |
| `state_b` | float64 | 7.0 |

## `concept_note`

Concept Note requirements by module and theme. Grain: requirement. Rows: 32.

| Column | Type | Example |
|---|---|---|
| `sno` | int64 | 1 |
| `module` | str | Membership |
| `theme` | str | Integration |
| `enhancement` | str | Integration with State family-ID portal  |
| `impact` | str | Transparency and Scope for enabling onli |
