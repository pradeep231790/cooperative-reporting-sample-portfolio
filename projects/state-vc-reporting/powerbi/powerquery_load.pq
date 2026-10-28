// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Create one query per block below, and one text parameter named DataFolder (Manage parameters).
// DataFolder must hold the full path of the powerbi/data folder, for example C:\repos\project\powerbi\data (no trailing backslash).

// ---- audit_progress_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\audit_progress_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"audit_20nov", Int64.Type}, {"audit_26nov", Int64.Type}, {"audit_3dec", Int64.Type}, {"total_pacs_dec18", Int64.Type}, {"audit_14nov", Int64.Type}, {"audit_18dec", Int64.Type}, {"audit_remaining_18dec", Int64.Type}})
in
    Typed

// ---- epacs_progress_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\epacs_progress_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"epacs_20nov", Int64.Type}, {"epacs_26nov", Int64.Type}, {"epacs_3dec", Int64.Type}, {"cert_14nov", Int64.Type}, {"entry_dayend_14nov", Int64.Type}, {"cert_18dec", Int64.Type}, {"entry_dayend_18dec", Int64.Type}})
in
    Typed

// ---- epacs_targets_dec2025
let
    Source = Csv.Document(File.Contents(DataFolder & "\epacs_targets_dec2025.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"t_27nov", Int64.Type}, {"t_4dec", Int64.Type}, {"t_11dec", Int64.Type}, {"t_15dec", Int64.Type}})
in
    Typed

// ---- state_timeline
let
    Source = Csv.Document(File.Contents(DataFolder & "\state_timeline.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"measure", type text}, {"source", type text}, {"date", type date}, {"value", Int64.Type}, {"total_pacs", Int64.Type}})
in
    Typed

// ---- weekly_audit_target_6nov
let
    Source = Csv.Document(File.Contents(DataFolder & "\weekly_audit_target_6nov.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total", Int64.Type}, {"audit_30oct", Int64.Type}, {"system_audit_yep", Int64.Type}, {"manual_audit", Int64.Type}, {"total_audit", Int64.Type}, {"remaining", Int64.Type}, {"pct_done", type number}, {"w1_target", type number}, {"w1_ach", Int64.Type}, {"w1_extra", type number}})
in
    Typed

// ---- weekly_epacs_target_6nov
let
    Source = Csv.Document(File.Contents(DataFolder & "\weekly_epacs_target_6nov.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total", Int64.Type}, {"t_30nov", Int64.Type}, {"t_25nov", Int64.Type}, {"t_20nov", Int64.Type}, {"t_15nov", Int64.Type}, {"w1_target", type number}, {"certified", type number}, {"w1_ach", Int64.Type}, {"w1_extra", type number}, {"pct_t1", type number}, {"w2_target", type number}, {"w2_ach", type number}, {"w3_target", type number}, {"w3_ach", type number}, {"w4_target", type number}, {"w4_ach", type number}})
in
    Typed

// ---- cert_pending_district_25jan2026
let
    Source = Csv.Document(File.Contents(DataFolder & "\cert_pending_district_25jan2026.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"pacs_listed", Int64.Type}, {"certificate_received", Int64.Type}, {"no_expected_date", Int64.Type}, {"certificate_pending", Int64.Type}})
in
    Typed

// ---- cert_expected_dates_25jan2026
let
    Source = Csv.Document(File.Contents(DataFolder & "\cert_expected_dates_25jan2026.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"expected", type date}, {"pacs", Int64.Type}})
in
    Typed
