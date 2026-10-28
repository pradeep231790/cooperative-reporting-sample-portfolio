"""training-status: builds the dashboards, Power BI kit and docs from the anonymised data in data/processed/.
python src/build.py"""
import sys, glob, zipfile, collections, warnings
from pathlib import Path
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]; PROC = ROOT / "data" / "processed"; sys.path.insert(0, str(Path(__file__).parent))
from scaffold import Project, PALETTE
up = lambda s: s.astype(str).str.strip().str.title()

rd = lambda n: pd.read_csv(PROC / n)
fe, rf, rdl, mo, ed, ev = [rd(n) for n in ["feb2026_district.csv", "refresher_district.csv", "refresher_daily.csv", "monthly_2025.csv", "edaksh_2024.csv", "evidence_by_district.csv"]]
P = Project(ROOT, "training-status", "Training Status: PACS Computerization, State A",
            "Training reach for PACS managers, operators, master trainers and auditors: monthly sessions in 2025, the Feb-2026 district round, refresher coverage and the 2024 e-Daksh baseline.",
            banner="Illustrative data: names are pseudonymised and counts are rescaled. The reporting design, KPIs and method are real; the numbers are not.",
            footer="Anonymised portfolio edition. Do not use these figures for decisions.")
ntr, npart = int(fe.trainings.sum()), int(fe.participants.sum()); dist_trained = int((fe.trainings > 0).sum()); nd = len(fe)
k1 = P.kpi("Trainings in Feb-2026 round", ntr, "int", "Training sessions reported by districts for February 2026", "Sum of Total Trainings", "SUM(feb2026_district[trainings])", "Source tracker", "cooperative registrar, development finance partner, state-level banking partner", home=True)
k2 = P.kpi("Participants in Feb-2026 round", npart, "int", "People trained in the February 2026 round", "Sum of Number of Participants", "SUM(feb2026_district[participants])", "Source tracker", "cooperative registrar, development finance partner", home=True)
k3 = P.kpi("Districts with a training (Feb-2026)", dist_trained, "int", f"Districts reporting at least one session, of {nd}", "Districts with trainings > 0", "CALCULATE(DISTINCTCOUNT(feb2026_district[district]), feb2026_district[trainings] > 0)", "Source tracker", "cooperative registrar, Collector", note=f"of {nd} districts", home=True)
k4 = P.kpi("Average participants per session", npart / max(ntr, 1), "dec1", "Mean attendance per Feb-2026 session", "Participants / Trainings", "DIVIDE([Participants in Feb-2026 round], [Trainings in Feb-2026 round])", "Source tracker", "Training coordinators")
k5 = P.kpi("Online share (Feb-2026)", 100 * fe.online.sum() / max(fe.online.sum() + fe.offline.sum(), 1), "pct1", "Online sessions as share of online + offline", "Online / (Online + Offline)", "DIVIDE(SUM(feb2026_district[online]), SUM(feb2026_district[online]) + SUM(feb2026_district[offline]))", "Source tracker", "Training coordinators")
tp, tw = int(rf.pacs.sum()), int(rf.pacs_with_training_date.sum())
k6 = P.kpi("Refresher coverage (PACS with a training date)", 100 * tw / tp, "pct1", "PACS whose staff have a training date in the 7-15 Feb refresher plan", "PACS with date / PACS listed", "DIVIDE(SUM(refresher_district[pacs_with_training_date]), SUM(refresher_district[pacs]))", "Source tracker", "cooperative registrar, development finance partner", tone="bad", home=True)
sess, att = int(mo.sessions.sum()), int(mo.attendance.sum())
k7 = P.kpi("Sessions May-Oct 2025", sess, "int", "Sessions with attendance recorded in the monthly trackers", "Rows with attendance > 0", "SUM(monthly_2025[sessions])", "Source tracker", "state-level banking partner, development finance partner")
k8 = P.kpi("Attendance May-Oct 2025", att, "int", "Total attendance recorded", "Sum of attendance counts", "SUM(monthly_2025[attendance])", "Source tracker", "state-level banking partner, development finance partner")
k9 = P.kpi("e-Daksh attendees 2024", int(ed.attendees.sum()), "int", "Attendees in the Feb-Mar 2024 baseline round", "Sum of attendee count", "SUM(edaksh_2024[attendees])", "Source tracker", "development finance partner")
P.table("feb2026_district", fe, "District-wise training counts, Feb 2026 (contacts removed)", "district"); P.table("refresher_district", rf, "Refresher coverage 7-15 Feb 2026 by district", "district"); P.table("refresher_daily", rdl, "PACS with a refresher training date, per day", "date")
P.table("monthly_2025", mo, "Monthly training sessions and attendance, May-Oct 2025", "month x audience"); P.table("edaksh_2024", ed, "e-Daksh training sessions 2024", "district"); P.table("evidence_by_district", ev, "Photo, PDF and video evidence file counts per district folder", "district folder")
P.relationships = ["`dim_district` is not required: join `feb2026_district[district]` to `refresher_district[district]` and `edaksh_2024[district]` on district name (many-to-one after de-duplication).", "`monthly_2025` and `refresher_daily` are standalone time tables (use month / date on the axis)."]
P.sources = [("District training tracker (Excel)", "District round: sessions, participants, role mix"), ("Refresher training plan (Excel)", "Coverage by district and by day (counts only)"), ("Monthly training trackers (Excel)", "Monthly sessions and attendance"), ("Baseline training list (Excel)", "First training round"), ("Training evidence archive", "Count of evidence files per district folder")]

P.exclusions = ["Real district, branch and bank names (replaced by pseudonyms).", "Original source files, PACS-level extracts, names, contact details and credentials.", "Real counts: all counts are rescaled, so absolute numbers are illustrative."]

P.assumptions = ["Districts showing 0 trainings may not have reported yet.", "Refresher coverage counts a PACS as covered when any training date is filled; it does not measure attendance. Dates typed with day and month swapped are corrected only when the swap lands in the plan month.", "Monthly sessions are rows with attendance above zero; mode spellings are normalised.", "Evidence counts show documentation, not the number of trainings held."]

S = lambda df, c, n=10, asc=False: [dict(label=r["district"], value=int(r[c])) for _, r in df.sort_values(c, ascending=asc).head(n).iterrows()]
rf["pct"] = (100 * rf.pacs_with_training_date / rf.pacs).round(1); zero = fe[fe.trainings == 0].district.tolist()
P.page("feb2026", "District training round (Feb-2026)", "Sessions, participants and role mix by district for the February 2026 round. Source: district training tracker.", [
    {"type": "kpis", "items": [k1, k2, k3, k4, k5]},
    {"type": "stack", "title": "Who was trained", "w": "half", "src": "feb2026_district", "parts": [dict(label=l, value=int(fe[c].sum()), color=PALETTE[i]) for i, (l, c) in enumerate([("PACS managers", "managers"), ("PACS operators", "operators"), ("Master trainers", "master_trainers"), ("Auditors", "auditors"), ("Others", "others")])]},
    {"type": "stack", "title": "Mode of training", "w": "half", "src": "feb2026_district", "parts": [dict(label="Online", value=int(fe.online.sum()), color=PALETTE[0]), dict(label="Offline", value=int(fe.offline.sum()), color=PALETTE[1])]},
    {"type": "hbars", "title": "Districts with most participants", "w": "half", "src": "feb2026_district", "rows": S(fe, "participants"), "color": "var(--c1)"},
    {"type": "text", "title": f"Districts with no training reported ({len(zero)})", "w": "half", "html": "<p style='margin:0'>" + (", ".join(zero) if zero else "None") + "</p>", "note": "These may be districts that have not yet reported."},
    {"type": "table", "title": "District table", "src": "feb2026_district", "search": "district", "cols": [dict(key="district", label="District"), dict(key="total_pacs", label="PACS", fmt="int"), dict(key="trainings", label="Trainings", fmt="int"), dict(key="participants", label="Participants", fmt="int"),
        dict(key="managers", label="Managers", fmt="int"), dict(key="operators", label="Operators", fmt="int"), dict(key="online", label="Online", fmt="int"), dict(key="offline", label="Offline", fmt="int"), dict(key="modules", label="Modules")], "rows": fe.to_dict("records"), "sort": "participants"}], tags=["cooperative registrar", "development finance partner", "state-level banking partner"])
P.page("refresher", "Refresher training coverage (7-15 Feb)", "How many PACS have a refresher training date in the plan, by district and by day.", [
    {"type": "kpis", "items": [k6, dict(label="PACS in refresher plan", value=f"{tp:,}"), dict(label="Districts below 50% coverage", value=str(int((rf.pct < 50).sum())), tone="bad"), dict(label="Dates outside Feb-2026 or unreadable", value=f"{tw - int(rdl[rdl.in_feb2026].pacs_trained.sum()):,}", note="data-quality check on the tracker")]},
    {"type": "line", "title": "PACS trained per day (Feb-2026)", "w": "half", "src": "refresher_daily", "labels": [d[5:] for d in rdl[rdl.in_feb2026].date], "series": [dict(name="PACS with training date", values=rdl[rdl.in_feb2026].pacs_trained.tolist(), color=PALETTE[0])]},
    {"type": "hbars", "title": "Lowest coverage (%)", "w": "half", "src": "refresher_district", "rows": [dict(label=r["district"], value=round(r.pct, 1)) for _, r in rf.sort_values("pct").head(10).iterrows()], "fmt": "pct1", "max": 100, "color": "var(--c3)"},
    {"type": "table", "title": "District coverage", "src": "refresher_district", "search": "district", "cols": [dict(key="district", label="District"), dict(key="pacs", label="PACS", fmt="int"), dict(key="pacs_with_training_date", label="With training date", fmt="int"),
        dict(key="pct", label="Coverage", fmt="pct1", heat=dict(lo=40, hi=80))], "rows": rf.to_dict("records"), "sort": "pct", "dir": 1}], tags=["cooperative registrar", "Collector"])
mm = mo.groupby("month").agg(sessions=("sessions", "sum"), attendance=("attendance", "sum"), online=("online", "sum"), offline=("offline", "sum")).reset_index()
P.page("monthly-2025", "Monthly trainings (May-Oct 2025)", "Sessions and attendance per month from the district trackers. Sep-Oct are tracked separately for managers and operators.", [
    {"type": "kpis", "items": [k7, k8, dict(label="Average attendance per session", value=f"{att / sess:.1f}")]},
    {"type": "line", "title": "Sessions and attendance by month", "w": "half", "src": "monthly_2025", "labels": mm.month.tolist(), "series": [dict(name="Attendance", values=mm.attendance.tolist(), color=PALETTE[0]), dict(name="Sessions", values=mm.sessions.tolist(), color=PALETTE[1])]},
    {"type": "stacks", "title": "Mode of training by month", "w": "half", "src": "monthly_2025", "groups": [dict(name=r.month, parts=[dict(label="Online", value=int(r.online), color=PALETTE[0]), dict(label="Offline", value=int(r.offline), color=PALETTE[1])]) for r in mm.itertuples()]},
    {"type": "table", "title": "Month and audience", "src": "monthly_2025", "cols": [dict(key="month", label="Month"), dict(key="audience", label="Audience"), dict(key="districts_covered", label="Districts", fmt="int"), dict(key="sessions", label="Sessions", fmt="int"), dict(key="attendance", label="Attendance", fmt="int")], "rows": mo.to_dict("records"), "sort": "month", "dir": 1}], tags=["state-level banking partner", "development finance partner"])
em = ed.assign(m=ed.training_date.str[:7]).groupby("m").agg(attendees=("attendees", "sum")).reset_index()
P.page("baseline-2024", "e-Daksh baseline (2024)", "The first training round before go-live: attendees by module, month and district.", [
    {"type": "kpis", "items": [k9, dict(label="Districts covered", value=str(ed.district.nunique())), dict(label="Modules", value=", ".join(sorted(ed.module.dropna().unique())))]},
    {"type": "line", "title": "Attendees by month", "w": "half", "src": "edaksh_2024", "labels": em.m.tolist(), "series": [dict(name="Attendees", values=em.attendees.tolist(), color=PALETTE[3])]},
    {"type": "hbars", "title": "Attendees by module", "w": "half", "src": "edaksh_2024", "rows": [dict(label=k, value=int(v)) for k, v in ed.groupby("module").attendees.sum().sort_values(ascending=False).items()], "color": "var(--c4)"},
    {"type": "table", "title": "District table", "src": "edaksh_2024", "search": "district", "cols": [dict(key="district", label="District"), dict(key="pacs_count", label="PACS", fmt="int"), dict(key="module", label="Module"), dict(key="training_date", label="Date"), dict(key="attendees", label="Attendees", fmt="int")], "rows": ed.fillna("").to_dict("records"), "sort": "attendees"}], tags=["development finance partner"])
evd = ev[ev.is_district]
P.page("evidence", "Training evidence by district", "How many photos and attendance PDFs are filed per district: a documentation check, not a count of trainings.", [
    {"type": "kpis", "items": [dict(label="District folders with evidence", value=str(len(evd))), dict(label="Photos", value=f"{int(ev.photos.sum()):,}"), dict(label="Attendance PDFs", value=f"{int(ev.attendance_pdf.sum()):,}")]},
    {"type": "hbars", "title": "Most evidence files", "w": "half", "src": "evidence_by_district", "rows": [dict(label=r.folder, value=int(r.photos + r.attendance_pdf + r.video + r.sheets + r.other)) for r in evd.sort_values("photos", ascending=False).head(12).itertuples()]},
    {"type": "table", "title": "All district folders", "w": "half", "src": "evidence_by_district", "search": "district", "cols": [dict(key="folder", label="Folder"), dict(key="photos", label="Photos", fmt="int"), dict(key="attendance_pdf", label="PDFs", fmt="int"), dict(key="sheets", label="Sheets", fmt="int")], "rows": ev.to_dict("records"), "sort": "photos"}], tags=["Audit trail"])
P.build()
