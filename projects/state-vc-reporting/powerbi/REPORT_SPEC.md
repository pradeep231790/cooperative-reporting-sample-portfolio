# Report specification: State VC Reporting: PACS Computerization, State A

Build one report page per section. Apply `theme.json` (View > Themes > Browse for themes).

## Page: Audit and YEP progress

State and district audit completion across the 20-Nov to 18-Dec review dates.

- **Card visuals (one per KPI)**: KPI cards: Audit and YEP completed (3-Dec-2025), Audit completion (3-Dec-2025), Audit gain in two weeks, Audit completion (18-Dec-2025)
- **Line chart**: Audit completed: state total by review date. Source: `state_timeline`
- **Clustered bar chart (sorted descending)**: Largest audit gain, 20-Nov to 3-Dec. Source: `audit_progress_district`
- **Clustered bar chart (sorted descending)**: Most PACS still pending audit (18-Dec). Source: `audit_progress_district`
- **Table or matrix with conditional formatting**: District table. Source: `audit_progress_district`

## Page: e-PACS completion and certification

e-PACS completed (4-Dec deck) and certificates issued (18-Dec deck) by district, with the dated Dec-2025 targets.

- **Card visuals (one per KPI)**: KPI cards: e-PACS completed (3-Dec-2025), e-PACS certificates (18-Dec-2025), e-PACS certificate growth
- **Line chart**: e-PACS completed (state). Source: `state_timeline`
- **Line chart**: e-PACS certificates (state). Source: `state_timeline`
- **Clustered bar chart (sorted descending)**: Dated targets: PACS due on each date (all PACS). Source: `epacs_targets_dec2025`
- **Clustered bar chart (sorted descending)**: Largest certificate growth, 14-Nov to 18-Dec. Source: `epacs_progress_district`
- **Table or matrix with conditional formatting**: District table. Source: `epacs_progress_district`

## Page: Weekly targets (6-Nov-2025)

The week-1 plan for audit and e-PACS by district and how much was achieved.

- **Card visuals (one per KPI)**: KPI cards: Week-1 e-PACS target achieved (6-Nov-2025), Audit week-1 achieved, Audit & YEP done (6-Nov)
- **Clustered bar chart (sorted descending)**: e-PACS: largest week-1 shortfall. Source: `weekly_epacs_target_6nov`
- **Clustered bar chart (sorted descending)**: Audit: largest week-1 shortfall. Source: `weekly_audit_target_6nov`
- **Table or matrix with conditional formatting**: e-PACS weekly target by district. Source: `weekly_epacs_target_6nov`
- **Table or matrix with conditional formatting**: Audit weekly target by district. Source: `weekly_audit_target_6nov`

## Page: Certification pending (25-Jan-2026)

PACS still waiting for their e-PACS certificate on 25-Jan-2026, with expected dates. District totals only.

- **Card visuals (one per KPI)**: KPI cards: PACS pending e-PACS certificate (25-Jan-2026), Districts with pending PACS, PACS with no expected date
- **Clustered bar chart (sorted descending)**: Pending PACS by district. Source: `cert_pending_district_25jan2026`
- **Clustered bar chart (sorted descending)**: Expected certificate date (PACS per date). Source: `cert_expected_dates_25jan2026`

## Page: VC slide pack: formats and KPIs

The standard slides used in the weekly State VC, the KPI each slide carries and the dashboard page that reproduces it.

- **Table or matrix with conditional formatting**: Slide formats
