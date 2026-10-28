// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Create one query per block below, and one text parameter named DataFolder (Manage parameters).
// DataFolder must hold the full path of the powerbi/data folder, for example C:\repos\project\powerbi\data (no trailing backslash).

// ---- dayend_snapshots
let
    Source = Csv.Document(File.Contents(DataFolder & "\dayend_snapshots.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"date", type date}, {"current", Int64.Type}, {"within_30d", Int64.Type}, {"avg_gap_days", type number}, {"total", Int64.Type}, {"current_Grp1", Int64.Type}, {"current_Grp2", Int64.Type}, {"current_Grp3", Int64.Type}})
in
    Typed

// ---- dayend_progress_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\dayend_progress_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total", Int64.Type}, {"current", Int64.Type}, {"current_first", Int64.Type}, {"avg_gap", type number}, {"gain", Int64.Type}})
in
    Typed

// ---- gap_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\gap_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total", Int64.Type}, {"avg_entry_gap", type number}, {"avg_dayend_gap", type number}, {"pct_entry_over_180", type number}})
in
    Typed

// ---- gap_bands
let
    Source = Csv.Document(File.Contents(DataFolder & "\gap_bands.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"measure", type text}, {"band", type text}, {"pacs", Int64.Type}})
in
    Typed

// ---- gap_groups
let
    Source = Csv.Document(File.Contents(DataFolder & "\gap_groups.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"group", type text}, {"pacs", Int64.Type}, {"avg_entry_gap", type number}, {"avg_dayend_gap", type number}})
in
    Typed

// ---- sep2025_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\sep2025_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"dct_done", Int64.Type}, {"golive", Int64.Type}, {"dayend_current", Int64.Type}, {"entries_30d", Int64.Type}, {"stale_180d", Int64.Type}, {"audit_fy25", Int64.Type}, {"yep_fy25", Int64.Type}, {"hoc", Int64.Type}, {"red", Int64.Type}, {"avg_health", type number}})
in
    Typed

// ---- sep2025_branch
let
    Source = Csv.Document(File.Contents(DataFolder & "\sep2025_branch.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"district cooperative bank", type text}, {"branch", type text}, {"total_pacs", Int64.Type}, {"dct_done", Int64.Type}, {"golive", Int64.Type}, {"dayend_current", Int64.Type}, {"entries_30d", Int64.Type}, {"stale_180d", Int64.Type}, {"audit_fy25", Int64.Type}, {"yep_fy25", Int64.Type}, {"hoc", Int64.Type}, {"red", Int64.Type}, {"avg_health", type number}})
in
    Typed

// ---- sep2025_bands
let
    Source = Csv.Document(File.Contents(DataFolder & "\sep2025_bands.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"band", type text}, {"pacs", Int64.Type}})
in
    Typed

// ---- working_status_3dec2025
let
    Source = Csv.Document(File.Contents(DataFolder & "\working_status_3dec2025.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"working", Int64.Type}, {"not_working", Int64.Type}, {"working_pct", type number}})
in
    Typed

// ---- laggards_3dec2025
let
    Source = Csv.Document(File.Contents(DataFolder & "\laggards_3dec2025.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"entry_on_or_before_31mar2025", Int64.Type}, {"dayend_on_or_before_31mar2025", Int64.Type}})
in
    Typed

// ---- dayend_month_3dec2025_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\dayend_month_3dec2025_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"dayend_2024", Int64.Type}, {"m01", type number}, {"m02", type number}, {"m03", type number}, {"m04", type number}, {"m05", type number}, {"m06", type number}, {"m07", type number}, {"m08", type number}, {"m09", type number}, {"m10", type number}, {"m11", type number}, {"m12", type number}, {"dayend_2025", Int64.Type}})
in
    Typed

// ---- dayend_month_3dec2025_state
let
    Source = Csv.Document(File.Contents(DataFolder & "\dayend_month_3dec2025_state.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"period", type text}, {"pacs", Int64.Type}})
in
    Typed

// ---- redzone_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\redzone_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"red_zone_pacs", Int64.Type}, {"yep_completed", Int64.Type}, {"ready_audit_25mar", Int64.Type}, {"ready_audit_30mar", Int64.Type}, {"avg_vouchers", type number}})
in
    Typed

// ---- redzone_reasons
let
    Source = Csv.Document(File.Contents(DataFolder & "\redzone_reasons.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"reason", type text}, {"pacs", Int64.Type}})
in
    Typed
