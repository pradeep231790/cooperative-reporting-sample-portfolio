# Report specification: Training Status: PACS Computerization, State A

Build one report page per section. Apply `theme.json` (View > Themes > Browse for themes).

## Page: District training round (Feb-2026)

Sessions, participants and role mix by district for the February 2026 round. Source: district training tracker.

- **Card visuals (one per KPI)**: KPI cards: Trainings in Feb-2026 round, Participants in Feb-2026 round, Districts with a training (Feb-2026), Average participants per session, Online share (Feb-2026)
- **100% stacked bar**: Who was trained. Source: `feb2026_district`
- **100% stacked bar**: Mode of training. Source: `feb2026_district`
- **Clustered bar chart (sorted descending)**: Districts with most participants. Source: `feb2026_district`
- **Text box**: Districts with no training reported (25)
- **Table or matrix with conditional formatting**: District table. Source: `feb2026_district`

## Page: Refresher training coverage (7-15 Feb)

How many PACS have a refresher training date in the plan, by district and by day.

- **Card visuals (one per KPI)**: KPI cards: Refresher coverage (PACS with a training date), PACS in refresher plan, Districts below 50% coverage, Dates outside Feb-2026 or unreadable
- **Line chart**: PACS trained per day (Feb-2026). Source: `refresher_daily`
- **Clustered bar chart (sorted descending)**: Lowest coverage (%). Source: `refresher_district`
- **Table or matrix with conditional formatting**: District coverage. Source: `refresher_district`

## Page: Monthly trainings (May-Oct 2025)

Sessions and attendance per month from the district trackers. Sep-Oct are tracked separately for managers and operators.

- **Card visuals (one per KPI)**: KPI cards: Sessions May-Oct 2025, Attendance May-Oct 2025, Average attendance per session
- **Line chart**: Sessions and attendance by month. Source: `monthly_2025`
- **100% stacked bar (one per group)**: Mode of training by month. Source: `monthly_2025`
- **Table or matrix with conditional formatting**: Month and audience. Source: `monthly_2025`

## Page: e-Daksh baseline (2024)

The first training round before go-live: attendees by module, month and district.

- **Card visuals (one per KPI)**: KPI cards: e-Daksh attendees 2024, Districts covered, Modules
- **Line chart**: Attendees by month. Source: `edaksh_2024`
- **Clustered bar chart (sorted descending)**: Attendees by module. Source: `edaksh_2024`
- **Table or matrix with conditional formatting**: District table. Source: `edaksh_2024`

## Page: Training evidence by district

How many photos and attendance PDFs are filed per district: a documentation check, not a count of trainings.

- **Card visuals (one per KPI)**: KPI cards: District folders with evidence, Photos, Attendance PDFs
- **Clustered bar chart (sorted descending)**: Most evidence files. Source: `evidence_by_district`
- **Table or matrix with conditional formatting**: All district folders. Source: `evidence_by_district`
