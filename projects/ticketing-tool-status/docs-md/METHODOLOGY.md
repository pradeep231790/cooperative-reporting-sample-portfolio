# Methodology and assumptions: Ticketing Tool Status: PACS Computerization, State A

## Assumptions to review

- Over-TAT limit is 2 days (`TAT_DAYS` in src/build.py). Replace with the SLA value.
- Pending counts by level may not add up to the stated total when a ticket is not attributed to a level in the source.
- Release status buckets are assigned by keyword from free-text status.
- Backlog age uses the `Days` field as given in the source.

## Data sources

| Source file | Used for |
|---|---|
| Ticket counter workbook | Raised, resolved and pending counters |
| Pending-issue list (Excel) | Backlog ageing by owner, category, module, district (aggregated) |
| Development task tracker (Excel) | Task priority, status, testing |
| Ticket category list (Excel) | Final taxonomy |
| Release status update (Excel) | Release item deployment status |
| Customization tracker (Excel) | Customization summary and open list |
| Weekly review issue log (Excel) | Recurring issues and actions |

## Deliberately excluded

- Real district, branch and bank names (replaced by pseudonyms).
- Original source files, PACS-level extracts, names, contact details and credentials.
- Real counts: all counts are rescaled, so absolute numbers are illustrative.
