# Data model: Policy Briefing: Cooperative Services Sample

## Tables

| Table | Grain | Description | Rows |
|---|---|---|---|
| `statea_scorecard` | metric | State scorecard metrics with date and source | 20 |
| `statea_progress_timeline` | date x measure | e-PACS progress at dated points (definitions differ by source) | 6 |
| `milestones` | event | Review milestones and deadlines | 12 |
| `policy_directions` | direction | policy briefing directions of 28-Jan-2026 with State A evidence | 6 |
| `integrations` | integration | Portal integrations and status | 9 |
| `statea_vs_stateb` | metric | State A vs State B progress, same metric | 3 |
| `statea_vs_stateb_scale` | metric | State A vs State B scale | 2 |
| `concept_note` | requirement | Concept Note requirements by module and theme | 32 |

## Columns

**statea_scorecard**: `metric`, `value`, `unit`, `as_of`, `source`

**statea_progress_timeline**: `date`, `measure`, `pacs`, `total_pacs`, `source`, `group`, `pct`

**milestones**: `date`, `event`, `source`

**policy_directions**: `no`, `area`, `direction`, `deadline`, `owner`, `statea_evidence`

**integrations**: `integration`, `purpose`, `status`

**statea_vs_stateb**: `metric`, `statea_pacs`, `statea_total`, `stateb_pacs`, `source`, `stateb_total`, `statea_pct`, `stateb_pct`

**statea_vs_stateb_scale**: `metric`, `state_a`, `state_b`

**concept_note**: `sno`, `module`, `theme`, `enhancement`, `impact`

## Relationships (create in Model view)

- All tables are independent; no relationships are required.
- Use `statea_scorecard[metric]` as a slicer or filter to pick KPI cards.
- `concept_note[module]` and `concept_note[theme]` are the axes for the enhancement charts.
