// Power Query (M). In Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Create one query per block below, and one text parameter named DataFolder (Manage parameters).
// DataFolder must hold the full path of the powerbi/data folder, for example C:\repos\project\powerbi\data (no trailing backslash).

// ---- statea_scorecard
let
    Source = Csv.Document(File.Contents(DataFolder & "\statea_scorecard.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"metric", type text}, {"value", type number}, {"unit", type text}, {"as_of", type date}, {"source", type text}})
in
    Typed

// ---- statea_progress_timeline
let
    Source = Csv.Document(File.Contents(DataFolder & "\statea_progress_timeline.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"date", type date}, {"measure", type text}, {"pacs", Int64.Type}, {"total_pacs", Int64.Type}, {"source", type text}, {"group", type text}, {"pct", type number}})
in
    Typed

// ---- milestones
let
    Source = Csv.Document(File.Contents(DataFolder & "\milestones.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"date", type date}, {"event", type text}, {"source", type text}})
in
    Typed

// ---- policy_directions
let
    Source = Csv.Document(File.Contents(DataFolder & "\policy_directions.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"no", Int64.Type}, {"area", type text}, {"direction", type text}, {"deadline", type text}, {"owner", type text}, {"statea_evidence", type text}})
in
    Typed

// ---- integrations
let
    Source = Csv.Document(File.Contents(DataFolder & "\integrations.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"integration", type text}, {"purpose", type text}, {"status", type text}})
in
    Typed

// ---- statea_vs_stateb
let
    Source = Csv.Document(File.Contents(DataFolder & "\statea_vs_stateb.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"metric", type text}, {"statea_pacs", Int64.Type}, {"statea_total", Int64.Type}, {"stateb_pacs", Int64.Type}, {"source", type text}, {"stateb_total", Int64.Type}, {"statea_pct", type number}, {"stateb_pct", type number}})
in
    Typed

// ---- statea_vs_stateb_scale
let
    Source = Csv.Document(File.Contents(DataFolder & "\statea_vs_stateb_scale.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"metric", type text}, {"state_a", type number}, {"state_b", type number}})
in
    Typed

// ---- concept_note
let
    Source = Csv.Document(File.Contents(DataFolder & "\concept_note.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"sno", Int64.Type}, {"module", type text}, {"theme", type text}, {"enhancement", type text}, {"impact", type text}})
in
    Typed
