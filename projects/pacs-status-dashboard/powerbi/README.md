# Power BI kit

This folder gives you everything needed to rebuild the dashboards in Power BI Desktop. **A ready-made .pbix file is not included** (it cannot be generated outside Power BI Desktop), and the DAX and Power Query here have not been run inside Power BI, so check each measure after loading.

1. Open Power BI Desktop > **Get data > Text/CSV** and load every file in `data/` (or use `powerquery_load.pq`).
2. Create relationships as listed in `MODEL.md`.
3. Create a blank table `_Measures` and paste the measures from `measures.dax`.
4. Apply `theme.json`.
5. Build pages following `REPORT_SPEC.md`.
