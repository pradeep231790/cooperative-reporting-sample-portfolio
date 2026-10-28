// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Create one query per block below, and one text parameter named DataFolder (Manage parameters).
// DataFolder must hold the full path of the powerbi/data folder, for example C:\repos\project\powerbi\data (no trailing backslash).

// ---- feb2026_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\feb2026_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"total_pacs", Int64.Type}, {"trainings", Int64.Type}, {"participants", Int64.Type}, {"managers", Int64.Type}, {"operators", Int64.Type}, {"master_trainers", Int64.Type}, {"auditors", Int64.Type}, {"others", Int64.Type}, {"online", Int64.Type}, {"offline", Int64.Type}, {"modules", type text}})
in
    Typed

// ---- refresher_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\refresher_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district", type text}, {"pacs", Int64.Type}, {"pacs_with_training_date", Int64.Type}, {"managers_listed", Int64.Type}, {"operators_listed", Int64.Type}})
in
    Typed

// ---- refresher_daily
let
    Source = Csv.Document(File.Contents(DataFolder & "\refresher_daily.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"date", type date}, {"pacs_trained", Int64.Type}, {"in_feb2026", type logical}})
in
    Typed

// ---- monthly_2025
let
    Source = Csv.Document(File.Contents(DataFolder & "\monthly_2025.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"month", type text}, {"audience", type text}, {"districts_covered", Int64.Type}, {"sessions", Int64.Type}, {"attendance", Int64.Type}, {"online", Int64.Type}, {"offline", Int64.Type}, {"hybrid", Int64.Type}})
in
    Typed

// ---- edaksh_2024
let
    Source = Csv.Document(File.Contents(DataFolder & "\edaksh_2024.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"district cooperative bank", type text}, {"district", type text}, {"pacs_count", Int64.Type}, {"module", type text}, {"training_date", type date}, {"attendees", Int64.Type}})
in
    Typed

// ---- evidence_by_district
let
    Source = Csv.Document(File.Contents(DataFolder & "\evidence_by_district.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"folder", type text}, {"sheets", Int64.Type}, {"photos", Int64.Type}, {"attendance_pdf", Int64.Type}, {"other", Int64.Type}, {"video", Int64.Type}, {"is_district", type logical}})
in
    Typed
