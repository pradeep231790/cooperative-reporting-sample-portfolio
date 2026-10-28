# KPI dictionary: PACS Status Dashboard: State A

One definition per KPI, so every report shows the same number.

| KPI | Definition | Formula | Source | Audience | Value in this build |
|---|---|---|---|---|---|
| **PACS with a current day-end (5-Nov-2025)** | PACS whose last day-end is on or after 31-Mar-2025 | Count of PACS | Source tracker | cooperative registrar, Collector, development finance partner | 1,851 |
| **Current day-end %** | Share of all PACS with a current day-end | Current / Total | Source tracker | cooperative registrar, Minister | 74.2% |
| **Gain since 29-Sep-2025** | Increase in current-day-end PACS from the first to the last snapshot | Latest - first | Source tracker | cooperative registrar | 952 |
| **Average day-end lag (days)** | Mean days between the snapshot date and each PACS's last day-end | Mean(snapshot - last day-end) | Source tracker | cooperative registrar, Collector | 235.6 |
| **Entry older than 180 days (6-Nov)** | PACS whose last entry is more than 180 days old | Entries >180d / Total | Source tracker | Collector, district cooperative bank | 48.2% |
| **Working PACS (3-Dec-2025)** | PACS working on the ERP as reported in the 4-Dec review | Working / Total | VC review deck 4-Dec-2025 | cooperative registrar, Collector | 54.1% |
| **Laggards: day-end on or before 31-Mar-2025** | PACS whose last day-end is 31-Mar-2025 or earlier (3-Dec) | Sum of district counts | VC review deck 4-Dec-2025 | Collector, district cooperative bank | 1,058 |
| **ERP go-live % (18-Sep-2025)** | PACS live on the ERP | Go-live / Total | Source tracker | Minister, development finance partner | 99.0% |
| **Red PACS (health score < 40, 18-Sep-2025)** | PACS with an analyst health score below 40 | Count where score < 40 | Source tracker | cooperative registrar, Collector | 1,736 |
| **Red Zone PACS (Nov-2025 list)** | PACS on the Red Zone list for audit | Rows in the list | Source tracker | cooperative registrar, Audit dept | 337 |
