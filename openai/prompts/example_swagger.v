pub struct SwaggerSpec {
pub mut:
    swagger      string
    info         Info
    host         string
    base_path    string   json:"basePath"
    schemes      []string
    consumes     []string
    produces     []string
    paths        map[string]PathItem
    definitions  map[string]Definition
}

pub struct Info {
pub mut:
    version      string
    title        string
    license      License
}

pub struct License {
pub mut:
    name         string
}

pub struct PathItem {
pub mut:
    get          Operation
    post         Operation
}

pub struct Operation {
pub mut:
    summary      string
    operation_id string   json:"operationId"
    tags         []string
    parameters   []Parameter
    responses    map[string]Response
}

pub struct Parameter {
pub mut:
    name         string
    in           string
    description  string
    required     bool
    type         string
    format       string
}

pub struct Response {
pub mut:
    description  string
    headers      map[string]Header
    schema       Schema
}

pub struct Header {
pub mut:
    type         string
    description  string
}

pub struct Schema {
pub mut:
    ref          string   json:"$ref"
}

pub struct Definition {
pub mut:
    required     []string
    properties   map[string]Property
}

pub struct Property {
pub mut:
    type         string
    format       string
}
