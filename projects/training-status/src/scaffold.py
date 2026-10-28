"""
Shared scaffold: one project definition -> dashboard site (docs/), Power BI kit (powerbi/), documentation (README + docs/*.md).
Each repo ships its own copy so it is fully self-contained.
"""
import json, re, shutil
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
PALETTE = ["#1F7A8C", "#D99A00", "#C0392B", "#6A5ACD", "#2E8B57", "#E07B39", "#5B717A", "#9CCBD4"]
VISUAL = {"kpis": "Card visuals (one per KPI)", "hbars": "Clustered bar chart (sorted descending)", "stack": "100% stacked bar", "stacks": "100% stacked bar (one per group)",
          "line": "Line chart", "table": "Table or matrix with conditional formatting", "text": "Text box"}

def fmtv(v, f):
    if v is None or (isinstance(v, float) and pd.isna(v)): return "-"
    if f == "pct1": return f"{v:.1f}%"
    if f == "pct2": return f"{v:.2f}%"
    if f == "dec1": return f"{v:,.1f}"
    if f == "int": return f"{int(round(v)):,}"
    return str(v)

class Project:
    def __init__(self, root, slug, title, subtitle, banner=None, footer=None, repo_url=None):
        self.root, self.slug, self.title, self.subtitle, self.banner, self.footer = Path(root), slug, title, subtitle, banner, footer
        self.repo_url = repo_url; self.pages, self.kpis, self.tables = [], [], {}
        self.sources, self.exclusions, self.assumptions, self.relationships, self.home_kpis = [], [], [], [], []

    # ---- registration
    def kpi(self, name, value, fmt, definition, formula, dax, source, audience, note=None, tone="", home=False):
        self.kpis.append(dict(name=name, definition=definition, formula=formula, dax=dax, source=source, audience=audience, value=fmtv(value, fmt)))
        card = dict(label=name, value=fmtv(value, fmt), note=note, tone=tone)
        if home: self.home_kpis.append(card)
        return card
    def table(self, name, df, desc, grain):
        self.tables[name] = dict(df=df.copy(), desc=desc, grain=grain)
    def page(self, id, title, intro, widgets, tags=None, nav=None):
        self.pages.append(dict(id=id, title=title, intro=intro, widgets=widgets, tags=tags or [], nav=nav))

    # ---- build
    def build(self):
        R = self.root; docs = R / "docs"; (docs / "assets").mkdir(parents=True, exist_ok=True); (docs / "data").mkdir(exist_ok=True)
        for f in ["app.css", "render.js"]: shutil.copy(HERE / "assets" / f, docs / "assets" / f)
        spec = dict(project=dict(title=self.title, subtitle=self.subtitle, banner=self.banner, footer=self.footer, kpis=self.home_kpis),
                    pages=[{k: v for k, v in p.items()} for p in self.pages])
        (docs / "data" / "spec.js").write_text("window.SPEC = " + json.dumps(spec, separators=(",", ":"), default=str) + ";", encoding="utf-8")
        shell = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                 '<title>{t}</title><link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Newsreader:wght@500;600&display=swap" rel="stylesheet">'
                 '<link rel="stylesheet" href="assets/app.css"></head><body data-page="{p}"><script src="data/spec.js"></script><script src="assets/render.js"></script></body></html>')
        (docs / "index.html").write_text(shell.format(t=self.title, p="index"), encoding="utf-8")
        for p in self.pages: (docs / f"{p['id']}.html").write_text(shell.format(t=f"{p['title']} | {self.title}", p=p["id"]), encoding="utf-8")
        (docs / ".nojekyll").write_text("")
        self._powerbi(); self._docs(); self._readme()
        print(f"[{self.slug}] pages={len(self.pages)} kpis={len(self.kpis)} tables={len(self.tables)}")

    def _powerbi(self):
        P = self.root / "powerbi"; (P / "data").mkdir(parents=True, exist_ok=True)
        theme = {"name": f"{self.title} theme", "dataColors": PALETTE, "background": "#FFFFFF", "foreground": "#14313B", "tableAccent": "#1F7A8C", "good": "#2E8B57", "neutral": "#D99A00", "bad": "#C0392B", "maximum": "#1F7A8C", "center": "#D99A00", "minimum": "#C0392B"}
        (P / "theme.json").write_text(json.dumps(theme, indent=2), encoding="utf-8")
        q = []
        for name, t in self.tables.items():
            df = t["df"]; df.to_csv(P / "data" / f"{name}.csv", index=False)
            types = []
            for c in df.columns:
                s = df[c]
                if pd.api.types.is_integer_dtype(s): ty = "Int64.Type"
                elif pd.api.types.is_float_dtype(s): ty = "type number"
                elif s.dtype == bool: ty = "type logical"
                elif s.dropna().astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$").all() and len(s.dropna()): ty = "type date"
                else: ty = "type text"
                types.append(f'{{"{c}", {ty}}}')
            q.append(f"// ---- {name}\nlet\n    Source = Csv.Document(File.Contents(DataFolder & \"\\{name}.csv\"), [Delimiter=\",\", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),\n"
                     f"    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),\n    Typed = Table.TransformColumnTypes(Promoted, {{{', '.join(types)}}})\nin\n    Typed\n")
        (P / "powerquery_load.pq").write_text("// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.\n"
            "// Create one query per block below, and one text parameter named DataFolder (Manage parameters).\n// DataFolder must hold the full path of the powerbi/data folder, for example C:\\repos\\project\\powerbi\\data (no trailing backslash).\n\n" + "\n".join(q), encoding="utf-8")
        dax = [f"// DAX measures for {self.title}", "// Create a table named _Measures (Enter data, blank) and add each measure below.", ""]
        for k in self.kpis:
            if k["dax"]: dax += [f"// {k['definition']}", f"{k['name']} = {k['dax']}", ""]
        (P / "measures.dax").write_text("\n".join(dax), encoding="utf-8")
        md = [f"# Data model: {self.title}", "", "## Tables", "", "| Table | Grain | Description | Rows |", "|---|---|---|---|"]
        md += [f"| `{n}` | {t['grain']} | {t['desc']} | {len(t['df']):,} |" for n, t in self.tables.items()]
        md += ["", "## Columns", ""]
        for n, t in self.tables.items(): md += [f"**{n}**: " + ", ".join(f"`{c}`" for c in t["df"].columns), ""]
        md += ["## Relationships (create in Model view)", ""] + [f"- {r}" for r in self.relationships] + [""]
        (P / "MODEL.md").write_text("\n".join(md), encoding="utf-8")
        rs = [f"# Report specification: {self.title}", "", "Build one report page per section. Apply `theme.json` (View > Themes > Browse for themes).", ""]
        for p in self.pages:
            rs += [f"## Page: {p['title']}", "", p["intro"], ""]
            for w in p["widgets"]:
                if w["type"] == "banner": continue
                ttl = w.get("title") or ("KPI cards: " + ", ".join(i["label"] for i in w.get("items", []))) if w["type"] == "kpis" else w.get("title", "")
                rs.append(f"- **{VISUAL.get(w['type'], w['type'])}**: {ttl}" + (f". Source: `{w['src']}`" if w.get("src") else "") + (f". Fields: {w['pbi']}" if w.get("pbi") else ""))
            rs.append("")
        (P / "REPORT_SPEC.md").write_text("\n".join(rs), encoding="utf-8")
        (P / "README.md").write_text(f"# Power BI kit\n\nThis folder gives you everything needed to rebuild the dashboards in Power BI Desktop. **A ready-made .pbix file is not included** (it cannot be generated outside Power BI Desktop), and the DAX and Power Query here have not been run inside Power BI, so check each measure after loading.\n\n1. Open Power BI Desktop > **Get data > Text/CSV** and load every file in `data/` (or use `powerquery_load.pq`).\n2. Create relationships as listed in `MODEL.md`.\n3. Create a blank table `_Measures` and paste the measures from `measures.dax`.\n4. Apply `theme.json`.\n5. Build pages following `REPORT_SPEC.md`.\n", encoding="utf-8")

    def _docs(self):
        D = self.root / "docs-md"; D.mkdir(exist_ok=True)
        k = [f"# KPI dictionary: {self.title}", "", "One definition per KPI, so every report shows the same number.", "", "| KPI | Definition | Formula | Source | Audience | Value in this build |", "|---|---|---|---|---|---|"]
        k += [f"| **{x['name']}** | {x['definition']} | {x['formula']} | {x['source']} | {x['audience']} | {x['value']} |" for x in self.kpis]
        (D / "KPI_DICTIONARY.md").write_text("\n".join(k) + "\n", encoding="utf-8")
        d = [f"# Data dictionary: {self.title}", "", "Tables in `data/processed/` (also copied to `powerbi/data/`). All are aggregated: no personal data.", ""]
        for n, t in self.tables.items():
            d += [f"## `{n}`", "", f"{t['desc']}. Grain: {t['grain']}. Rows: {len(t['df']):,}.", "", "| Column | Type | Example |", "|---|---|---|"]
            for c in t["df"].columns:
                s = t["df"][c].dropna(); d.append(f"| `{c}` | {t['df'][c].dtype} | {str(s.iloc[0])[:40] if len(s) else ''} |")
            d.append("")
        (D / "DATA_DICTIONARY.md").write_text("\n".join(d), encoding="utf-8")
        m = [f"# Methodology and assumptions: {self.title}", "", "## Assumptions to review", ""] + [f"- {a}" for a in self.assumptions] + ["", "## Data sources", "", "| Source file | Used for |", "|---|---|"] + [f"| {a} | {b} |" for a, b in self.sources]
        m += ["", "## Deliberately excluded", ""] + [f"- {e}" for e in self.exclusions] + [""]
        (D / "METHODOLOGY.md").write_text("\n".join(m), encoding="utf-8")

    def _readme(self):
        r = [f"# {self.title}", "", self.subtitle.replace("<b>", "**").replace("</b>", "**"), ""]
        if self.repo_url: r += [f"Live dashboard (after enabling GitHub Pages on `/docs`): {self.repo_url}", ""]
        r += ["## Dashboards", "", "| Page | What it answers |", "|---|---|"] + [f"| `docs/{p['id']}.html` | {p['title']}: {re.sub('<[^>]+>', '', p['intro'])} |" for p in self.pages]
        r += ["", "## Headline KPIs", "", "| KPI | Value | Definition |", "|---|---|---|"] + [f"| {x['name']} | {x['value']} | {x['definition']} |" for x in self.kpis[:10]]
        r += ["", "Full list: [docs-md/KPI_DICTIONARY.md](docs-md/KPI_DICTIONARY.md).", "", "## Data sources", "", "| Source file | Used for |", "|---|---|"] + [f"| {a} | {b} |" for a, b in self.sources]
        r += ["", "## Run it", "", "```bash", "pip install -r requirements.txt", "python src/build.py                 # rebuild site, Power BI kit and docs from data/processed/", "```",
              "Open `docs/index.html` in a browser. No server is needed.", "", "## Power BI", "", "See [powerbi/README.md](powerbi/README.md): data model, DAX measures, Power Query loader, theme and a page-by-page report specification.",
              "", "## Privacy", "", "This is an anonymised portfolio edition:", ""] + [f"- {e}" for e in self.exclusions]
        r += ["", "## Assumptions", ""] + [f"- {a}" for a in self.assumptions] + ["", "## Documentation", "", "- [KPI dictionary](docs-md/KPI_DICTIONARY.md)", "- [Data dictionary](docs-md/DATA_DICTIONARY.md)", "- [Methodology](docs-md/METHODOLOGY.md)", ""]
        (self.root / "README.md").write_text("\n".join(r), encoding="utf-8")
