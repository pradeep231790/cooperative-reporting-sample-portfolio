// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Create one query per block below, and one text parameter named DataFolder (Manage parameters).
// DataFolder must hold the full path of the powerbi/data folder, for example C:\repos\project\powerbi\data (no trailing backslash).

// ---- tickets_summary
let
    Source = Csv.Document(File.Contents(DataFolder & "\tickets_summary.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"metric", type text}, {"value", Int64.Type}, {"group", type text}})
in
    Typed

// ---- backlog_nov2025
let
    Source = Csv.Document(File.Contents(DataFolder & "\backlog_nov2025.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"dimension", type text}, {"key", type text}, {"tickets", Int64.Type}, {"over_tat", Int64.Type}, {"avg_age", type number}})
in
    Typed

// ---- backlog_nov2025_side_age
let
    Source = Csv.Document(File.Contents(DataFolder & "\backlog_nov2025_side_age.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"side", type text}, {"age_band", type text}, {"tickets", Int64.Type}})
in
    Typed

// ---- dev_tasks_summary
let
    Source = Csv.Document(File.Contents(DataFolder & "\dev_tasks_summary.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"dimension", type text}, {"key", type text}, {"tasks", Int64.Type}, {"avg_days_to_complete", type number}})
in
    Typed

// ---- dev_tasks_timeline
let
    Source = Csv.Document(File.Contents(DataFolder & "\dev_tasks_timeline.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"month", type text}, {"tasks_started", Int64.Type}, {"tasks_completed", Int64.Type}})
in
    Typed

// ---- taxonomy
let
    Source = Csv.Document(File.Contents(DataFolder & "\taxonomy.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"nature", type text}, {"sub_nature", type text}, {"priority", type text}})
in
    Typed

// ---- release_notes_status
let
    Source = Csv.Document(File.Contents(DataFolder & "\release_notes_status.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"sno", type text}, {"item", type text}, {"status_dec", type text}, {"status_jan", type text}, {"bucket_dec", type text}, {"bucket_jan", type text}})
in
    Typed

// ---- customizations_summary
let
    Source = Csv.Document(File.Contents(DataFolder & "\customizations_summary.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"metric", type text}, {"value", Int64.Type}})
in
    Typed

// ---- customizations_open
let
    Source = Csv.Document(File.Contents(DataFolder & "\customizations_open.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"cui", type text}, {"customization", type text}, {"assigned_to", type text}, {"start", type date}, {"age_days", Int64.Type}})
in
    Typed

// ---- weekly_review_issues
let
    Source = Csv.Document(File.Contents(DataFolder & "\weekly_review_issues.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"sno", Int64.Type}, {"issue", type text}, {"action_required", type text}})
in
    Typed
