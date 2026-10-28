# Report specification: Ticketing Tool Status: PACS Computerization, State A

Build one report page per section. Apply `theme.json` (View > Themes > Browse for themes).

## Page: Ticket overview and resolution

How many tickets were raised, who raised them, who resolved them and what is still open. Source: Issue List.

- **Card visuals (one per KPI)**: KPI cards: Tickets raised, Tickets resolved, Resolution rate, Pending tickets, Resolved at first level (L1), Resolved by Vendor (software vendor)
- **100% stacked bar**: Who resolved the tickets. Source: `tickets_summary`
- **100% stacked bar**: Who raised the tickets. Source: `tickets_summary`
- **Clustered bar chart (sorted descending)**: Pending tickets by level. Source: `tickets_summary`
- **Clustered bar chart (sorted descending)**: Backlog then and now

## Page: Backlog ageing (6-Nov-2025)

Open tickets by owner, age and cluster. Over-TAT means older than 2 days (assumed).

- **Card visuals (one per KPI)**: KPI cards: Backlog on 6-Nov-2025, Backlog over TAT (6-Nov-2025), With Vendor
- **100% stacked bar (one per group)**: Owner by age of ticket. Source: `backlog_nov2025_side_age`
- **Clustered bar chart (sorted descending)**: By category. Source: `backlog_nov2025`
- **Clustered bar chart (sorted descending)**: By module. Source: `backlog_nov2025`
- **Clustered bar chart (sorted descending)**: By issue subject. Source: `backlog_nov2025`
- **Clustered bar chart (sorted descending)**: Districts with most open tickets. Source: `backlog_nov2025`
- **Table or matrix with conditional formatting**: Ten oldest open tickets

## Page: Ticket taxonomy and development tasks

The category structure used to log tickets, and the tracker of tool-development tasks (priority, status, testing).

- **Card visuals (one per KPI)**: KPI cards: Dev tasks completed, Highest-priority tasks (P0), Tasks with testing pending
- **Clustered bar chart (sorted descending)**: Sub-natures by nature. Source: `taxonomy`
- **100% stacked bar**: Taxonomy priority. Source: `taxonomy`
- **100% stacked bar (one per group)**: Task status and testing. Source: `dev_tasks_summary`
- **Line chart**: Tasks started and completed per month. Source: `dev_tasks_timeline`

## Page: Releases and customizations

Deployment status of release 1.0.5.6 and the customization request pipeline. Sources: release-notes status update and State A Customizations tracker.

- **Card visuals (one per KPI)**: KPI cards: Customizations resolved, Requested, Pending at Vendor, On hold
- **100% stacked bar (one per group)**: Release 1.0.5.6 status: 22-Dec-2025 vs 12-Jan-2026. Source: `release_notes_status`
- **Clustered bar chart (sorted descending)**: Customization requests by status. Source: `customizations_summary`
- **Table or matrix with conditional formatting**: Open customizations (age on 3-Dec-2025). Source: `customizations_open`
- **Table or matrix with conditional formatting**: Release 1.0.5.6 items. Source: `release_notes_status`

## Page: Weekly review issue log (12-Sep-2024)

Issues raised in the weekly review meeting and the action required: a model for recording recurring issues with an owner.

- **Table or matrix with conditional formatting**: Issues and actions. Source: `weekly_review_issues`
