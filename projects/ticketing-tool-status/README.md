# Ticketing Tool Status: PACS Computerization, State A

Support-ticket volumes, resolution by level (L1, L2, Vendor), backlog ageing, development tasks, release deployment and customization status for the e-PACS ERP rollout.

## Dashboards

| Page | What it answers |
|---|---|
| `docs/overview.html` | Ticket overview and resolution: How many tickets were raised, who raised them, who resolved them and what is still open. Source: Issue List. |
| `docs/backlog.html` | Backlog ageing (6-Nov-2025): Open tickets by owner, age and cluster. Over-TAT means older than 2 days (assumed). |
| `docs/taxonomy.html` | Ticket taxonomy and development tasks: The category structure used to log tickets, and the tracker of tool-development tasks (priority, status, testing). |
| `docs/releases.html` | Releases and customizations: Deployment status of release 1.0.5.6 and the customization request pipeline. Sources: release-notes status update and State A Customizations tracker. |
| `docs/review-log.html` | Weekly review issue log (12-Sep-2024): Issues raised in the weekly review meeting and the action required: a model for recording recurring issues with an owner. |

## Headline KPIs

| KPI | Value | Definition |
|---|---|---|
| Tickets raised | 50,460 | All support tickets logged in the ticketing tool |
| Tickets resolved | 50,453 | Tickets closed at any level |
| Resolution rate | 99.99% | Share of raised tickets resolved |
| Pending tickets | 7 | Tickets still open |
| Resolved at first level (L1) | 31.7% | Share of resolutions closed by the L1 support centre |
| Resolved by Vendor (software vendor) | 48.9% | Share needing vendor-side fixes |
| Backlog on 6-Nov-2025 | 88 | Open tickets in the Vendor-side pending list |
| Backlog over TAT (6-Nov-2025) | 22 | Open tickets older than 2 days (assumed TAT) |
| Dev tasks completed | 54.5% | Completed development tasks as share of the tracker |
| Customizations resolved | 54.4% | Resolved customization requests as share of all requested |

Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).

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

## Run it

```bash
pip install -r requirements.txt
python src/build.py                 # rebuild site, Power BI kit and docs from data/processed/
```
Open `docs/index.html` in a browser. No server is needed.

## Power BI

See [powerbi/README.md](powerbi/README.md): data model, DAX measures, Power Query loader, theme and a page-by-page report specification.

## Privacy

This is an anonymised portfolio edition:

- Real district, branch and bank names (replaced by pseudonyms).
- Original source files, PACS-level extracts, names, contact details and credentials.
- Real counts: all counts are rescaled, so absolute numbers are illustrative.

## Assumptions

- Over-TAT limit is 2 days (`TAT_DAYS` in src/build.py). Replace with the SLA value.
- Pending counts by level may not add up to the stated total when a ticket is not attributed to a level in the source.
- Release status buckets are assigned by keyword from free-text status.
- Backlog age uses the `Days` field as given in the source.

## Documentation

- [KPI dictionary](docs-md/KPI_DICTIONARY.md)
- [Data dictionary](docs-md/DATA_DICTIONARY.md)
- [Methodology](docs-md/METHODOLOGY.md)
