"""ticketing-tool-status: builds the dashboards, Power BI kit and docs from the anonymised data in data/processed/.
python src/build.py"""
import sys, re, glob, warnings
from pathlib import Path
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]; PROC = ROOT / "data" / "processed"; sys.path.insert(0, str(Path(__file__).parent))
from scaffold import Project, PALETTE
TAT_DAYS = 2   # ASSUMPTION: a ticket is 'over TAT' after 2 days; replace with the SLA value

rd = lambda n: pd.read_csv(PROC / n)
ts, bl, bsa, old, dts, dtl, tx, rn, cs, co, wr = [rd(n) for n in ["tickets_summary.csv", "backlog_nov2025.csv", "backlog_nov2025_side_age.csv", "backlog_nov2025_oldest.csv", "dev_tasks_summary.csv", "dev_tasks_timeline.csv", "taxonomy.csv", "release_notes_status.csv", "customizations_summary.csv", "customizations_open.csv", "weekly_review_issues_2024-09-12.csv"]]
V = dict(zip(ts.metric, ts.value)); raised, resolved, pend = V["Total Issue Raised"], V["Total Issue Resolved"], V["Total Pending Issue"]
C = dict(zip(cs.metric, cs.value))
P = Project(ROOT, "ticketing-tool-status", "Ticketing Tool Status: PACS Computerization, State A",
            "Support-ticket volumes, resolution by level (L1, L2, Vendor), backlog ageing, development tasks, release deployment and customization status for the e-PACS ERP rollout.",
            banner="Illustrative data: names are pseudonymised and counts are rescaled. The reporting design, KPIs and method are real; the numbers are not.",
            footer="Anonymised portfolio edition. Do not use these figures for decisions.")
# ---- KPIs
k1 = P.kpi("Tickets raised", raised, "int", "All support tickets logged in the ticketing tool", "Count of tickets", 'CALCULATE(SUM(tickets_summary[value]), tickets_summary[metric] = "Total Issue Raised")', "Source tracker", "development finance partner, state-level banking partner, cooperative registrar", home=True)
k2 = P.kpi("Tickets resolved", resolved, "int", "Tickets closed at any level", "Count of tickets", 'CALCULATE(SUM(tickets_summary[value]), tickets_summary[metric] = "Total Issue Resolved")', "Source tracker", "development finance partner, state-level banking partner", home=True)
k3 = P.kpi("Resolution rate", 100 * resolved / raised, "pct2", "Share of raised tickets resolved", "Resolved / Raised", "DIVIDE([Tickets resolved], [Tickets raised])", "Source tracker", "All", tone="good", home=True)
k4 = P.kpi("Pending tickets", pend, "int", "Tickets still open", "Count of tickets", 'CALCULATE(SUM(tickets_summary[value]), tickets_summary[metric] = "Total Pending Issue")', "Source tracker", "Vendor, SI", home=True)
shares = {k: V[f"Total Issue Resolved by {k}"] for k in ["L1", "L2", "Vendor"]}
k5 = P.kpi("Resolved at first level (L1)", 100 * shares["L1"] / resolved, "pct1", "Share of resolutions closed by the L1 support centre", "L1 resolved / Resolved", 'DIVIDE(CALCULATE(SUM(tickets_summary[value]), tickets_summary[metric] = "Total Issue Resolved by L1"), [Tickets resolved])', "Source tracker", "SI, development finance partner")
k6 = P.kpi("Resolved by Vendor (software vendor)", 100 * shares["Vendor"] / resolved, "pct1", "Share needing vendor-side fixes", "Vendor resolved / Resolved", 'DIVIDE(CALCULATE(SUM(tickets_summary[value]), tickets_summary[metric] = "Total Issue Resolved by Vendor"), [Tickets resolved])', "Source tracker", "Vendor, development finance partner", tone="bad")
b = bl[bl.dimension == "side"].set_index("key"); nov_total = int(b.tickets.sum()); over = int(b.over_tat.sum())
k7 = P.kpi("Backlog on 6-Nov-2025", nov_total, "int", "Open tickets in the Vendor-side pending list", "Count of open tickets", "SUM(backlog_nov2025[tickets])", "Source tracker", "state-level banking partner, Vendor")
k8 = P.kpi("Backlog over TAT (6-Nov-2025)", over, "int", f"Open tickets older than {TAT_DAYS} days (assumed TAT)", "Tickets with age > TAT", 'CALCULATE(SUM(backlog_nov2025[over_tat]), backlog_nov2025[dimension] = "side")', "Source tracker", "Vendor", tone="bad")
dd = dts[dts.dimension == "status"].set_index("key").tasks; dp = dts[dts.dimension == "priority"].set_index("key").tasks; dtst = dts[dts.dimension == "testing"].set_index("key").tasks
k9 = P.kpi("Dev tasks completed", 100 * dd.get("Completed", 0) / dd.sum(), "pct1", "Completed development tasks as share of the tracker", "Completed / All tasks", 'DIVIDE(CALCULATE(SUM(dev_tasks_summary[tasks]), dev_tasks_summary[dimension] = "status", dev_tasks_summary[key] = "Completed"), CALCULATE(SUM(dev_tasks_summary[tasks]), dev_tasks_summary[dimension] = "status"))', "Source tracker", "SI, state-level banking partner")
k10 = P.kpi("Customizations resolved", 100 * C["Resolved"] / C["Total Customizations Requested"], "pct1", "Resolved customization requests as share of all requested", "Resolved / Requested", 'DIVIDE(CALCULATE(SUM(customizations_summary[value]), customizations_summary[metric] = "Resolved"), CALCULATE(SUM(customizations_summary[value]), customizations_summary[metric] = "Total Customizations Requested"))', "Source tracker", "Vendor, state-level banking partner, development finance partner")
# ---- tables
P.table("tickets_summary", ts, "Ticket counters: raised, resolved, pending by level", "one row per metric")
P.table("backlog_nov2025", bl, "Open-ticket backlog on 6-Nov-2025, long format by dimension", "dimension x key")
P.table("backlog_nov2025_side_age", bsa, "Open tickets by owner and age band", "side x age band")
P.table("dev_tasks_summary", dts, "Development task tracker, long format by dimension", "dimension x key")
P.table("dev_tasks_timeline", dtl, "Development tasks started and completed per month", "month")
P.table("taxonomy", tx, "Ticket category taxonomy: nature, sub-nature, priority", "sub-nature")
P.table("release_notes_status", rn, "Release 1.0.5.6 items with deployment status on 22-Dec-2025 and 12-Jan-2026", "release item")
P.table("customizations_summary", cs, "Customization counts by status", "one row per status")
P.table("customizations_open", co, "Open customization requests with age", "customization")
P.relationships = ["`backlog_nov2025` and `backlog_nov2025_side_age` are independent fact tables (filter by `dimension` / `side`).", "`dev_tasks_summary[key]` is filtered together with `dimension`: always add a visual-level filter on `dimension`.", "All tables are small and unrelated; no relationships are required."]
P.sources = [("Ticket counter workbook", "Raised, resolved and pending counters"), ("Pending-issue list (Excel)", "Backlog ageing by owner, category, module, district (aggregated)"), ("Development task tracker (Excel)", "Task priority, status, testing"), ("Ticket category list (Excel)", "Final taxonomy"), ("Release status update (Excel)", "Release item deployment status"), ("Customization tracker (Excel)", "Customization summary and open list"), ("Weekly review issue log (Excel)", "Recurring issues and actions")]

P.exclusions = ["Real district, branch and bank names (replaced by pseudonyms).", "Original source files, PACS-level extracts, names, contact details and credentials.", "Real counts: all counts are rescaled, so absolute numbers are illustrative."]

P.assumptions = [f"Over-TAT limit is {TAT_DAYS} days (`TAT_DAYS` in src/build.py). Replace with the SLA value.", "Pending counts by level may not add up to the stated total when a ticket is not attributed to a level in the source.", "Release status buckets are assigned by keyword from free-text status.", "Backlog age uses the `Days` field as given in the source."]

# ---- pages
side = bl[bl.dimension == "side"]; top = lambda dim, n: [dict(label=r.key, value=int(r.tickets)) for r in bl[bl.dimension == dim].sort_values("tickets", ascending=False).head(n).itertuples()]
bc = {"Same day": "#2E8B57", "1-2 days": "#9CCF6B", "3-7 days": "#D99A00", ">7 days": "#C0392B"}
P.page("overview", "Ticket overview and resolution", "How many tickets were raised, who raised them, who resolved them and what is still open. Source: Issue List.", [
    {"type": "kpis", "items": [k1, k2, k3, k4, k5, k6]},
    {"type": "stack", "title": "Who resolved the tickets", "w": "half", "src": "tickets_summary", "parts": [dict(label=k, value=int(v), color=c) for (k, v), c in zip(shares.items(), PALETTE)], "note": "L1 = first-level support centre, L2 = regional manager, Vendor = software vendor."},
    {"type": "stack", "title": "Who raised the tickets", "w": "half", "src": "tickets_summary", "parts": [dict(label="PACS", value=int(V["Total Issue Raised by Pacs"]), color=PALETTE[0]), dict(label="L1 support", value=int(V["Total Issue Raised by L1"]), color=PALETTE[1])]},
    {"type": "hbars", "title": "Pending tickets by level", "w": "half", "src": "tickets_summary", "rows": [dict(label=k, value=int(V[f"Total Pending Issue at {k}"])) for k in ["L1", "L2", "Vendor"]], "color": "var(--c3)", "note": "One pending ticket is not attributed to a level in the source."},
    {"type": "hbars", "title": "Backlog then and now", "w": "half", "rows": [dict(label="6-Nov-2025 backlog", value=nov_total, color="var(--c3)"), dict(label="Issue List (closing)", value=int(pend), color="var(--c1)")], "note": "Different files; both describe open tickets."}], tags=["development finance partner", "state-level banking partner", "cooperative registrar"])
P.page("backlog", "Backlog ageing (6-Nov-2025)", f"Open tickets by owner, age and cluster. Over-TAT means older than {TAT_DAYS} days (assumed).", [
    {"type": "kpis", "items": [k7, k8, dict(label="With Vendor", value=str(int(side[side.key == "With Vendor"].tickets.sum())), tone="bad")]},
    {"type": "stacks", "title": "Owner by age of ticket", "w": "half", "src": "backlog_nov2025_side_age", "groups": [dict(name=s, parts=[dict(label=a, value=int(bsa[(bsa.side == s) & (bsa.age_band == a)].tickets.sum()), color=bc[a]) for a in bc]) for s in bsa.side.unique()]},
    {"type": "hbars", "title": "By category", "w": "half", "rows": top("category", 8), "src": "backlog_nov2025"},
    {"type": "hbars", "title": "By module", "w": "half", "rows": top("module", 10), "color": "var(--c4)", "src": "backlog_nov2025"},
    {"type": "hbars", "title": "By issue subject", "w": "half", "rows": top("subject", 10), "color": "var(--c2)", "src": "backlog_nov2025"},
    {"type": "hbars", "title": "Districts with most open tickets", "w": "half", "rows": top("district", 10), "color": "var(--c3)", "src": "backlog_nov2025"},
    {"type": "table", "title": "Ten oldest open tickets", "w": "half", "cols": [dict(key="district", label="District"), dict(key="module", label="Module"), dict(key="side", label="With"), dict(key="age_days", label="Age (days)", fmt="int")], "rows": old.to_dict("records"), "sort": "age_days"}], tags=["state-level banking partner", "Vendor"])
P.page("taxonomy", "Ticket taxonomy and development tasks", "The category structure used to log tickets, and the tracker of tool-development tasks (priority, status, testing).", [
    {"type": "kpis", "items": [k9, dict(label="Highest-priority tasks (P0)", value=str(int(dp.get("P0", 0)))), dict(label="Tasks with testing pending", value=str(int(dtst.get("Pending", 0))), tone="bad")]},
    {"type": "hbars", "title": "Sub-natures by nature", "w": "half", "src": "taxonomy", "rows": [dict(label=k, value=int(v)) for k, v in tx.groupby("nature").size().sort_values(ascending=False).items()]},
    {"type": "stack", "title": "Taxonomy priority", "w": "half", "src": "taxonomy", "parts": [dict(label=k, value=int(v), color=PALETTE[i]) for i, (k, v) in enumerate(tx.priority.value_counts().items())]},
    {"type": "stacks", "title": "Task status and testing", "w": "half", "src": "dev_tasks_summary", "groups": [dict(name=d.title(), parts=[dict(label=r.key, value=int(r.tasks), color=PALETTE[i % 8]) for i, r in enumerate(dts[dts.dimension == d].itertuples())]) for d in ["status", "testing", "priority"]]},
    {"type": "line", "title": "Tasks started and completed per month", "w": "half", "src": "dev_tasks_timeline", "labels": dtl.month.tolist(), "series": [dict(name="Started", values=dtl.tasks_started.tolist(), color=PALETTE[0]), dict(name="Completed", values=dtl.tasks_completed.tolist(), color=PALETTE[4])]}], tags=["SI", "state-level banking partner"])
bj = rn.bucket_jan.value_counts(); bd = rn.bucket_dec.value_counts(); cc = [(k, int(v)) for k, v in C.items()]
P.page("releases", "Releases and customizations", "Deployment status of release 1.0.5.6 and the customization request pipeline. Sources: release-notes status update and State A Customizations tracker.", [
    {"type": "kpis", "items": [k10, dict(label="Requested", value=str(int(C["Total Customizations Requested"]))), dict(label="Pending at Vendor", value=str(int(C.get("Pending at Vendor", 0))), tone="bad"), dict(label="On hold", value=str(int(C.get("On Hold", 0))))]},
    {"type": "stacks", "title": "Release 1.0.5.6 status: 22-Dec-2025 vs 12-Jan-2026", "w": "half", "src": "release_notes_status", "groups": [dict(name=n, parts=[dict(label=k, value=int(s.get(k, 0)), color=PALETTE[i]) for i, k in enumerate(["Deployed / working", "Partly deployed", "Needs clarification", "Not deployed", "Issue persists", "Other"]) if s.get(k, 0)]) for n, s in [("22-Dec-2025", bd), ("12-Jan-2026", bj)]]},
    {"type": "hbars", "title": "Customization requests by status", "w": "half", "src": "customizations_summary", "rows": [dict(label=k, value=v) for k, v in cc if k != "Total Customizations Requested"]},
    {"type": "table", "title": "Open customizations (age on 3-Dec-2025)", "src": "customizations_open", "search": "customization", "cols": [dict(key="customization", label="Customization"), dict(key="assigned_to", label="Assigned to"), dict(key="age_days", label="Age (days)", fmt="int")], "rows": co.fillna("").to_dict("records"), "sort": "age_days", "maxh": 380},
    {"type": "table", "title": "Release 1.0.5.6 items", "src": "release_notes_status", "search": "item", "cols": [dict(key="item", label="Item"), dict(key="bucket_dec", label="Dec-2025"), dict(key="bucket_jan", label="Jan-2026")], "rows": rn.to_dict("records"), "sort": "sno", "dir": 1, "maxh": 380}], tags=["Vendor", "development finance partner", "state-level banking partner"])
P.page("review-log", "Weekly review issue log (12-Sep-2024)", "Issues raised in the weekly review meeting and the action required: a model for recording recurring issues with an owner.", [
    {"type": "table", "title": "Issues and actions", "src": "weekly_review_issues", "cols": [dict(key="issue", label="Issue"), dict(key="action_required", label="Action required")], "rows": wr.fillna("").to_dict("records"), "sort": "sno", "dir": 1}], tags=["Weekly review"])
P.table("weekly_review_issues", wr, "Issues discussed in the 12-Sep-2024 weekly review", "issue")
P.build()
