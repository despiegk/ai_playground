
a line starting with fn, its a function, the text after it gives content to that function

I will give you some information about modules in V which might be useful and can be used by you to create code, each module definition starts with """MODULE and the name of the module on same line
and ends with """MODULE END

inside there can be line starting with EXAMPLE: which will  show how to use it


"""MODULE json
fn decode(typ voidptr, s string) !voidptr
decode tries to decode the provided JSON string, into a V structure.
If it can not do that, it returns an error describing the reason fort he parsing failure.

fn encode(x voidptr) string
encode serialises the provided V value as a JSON string, optimised for shortness.

EXAMPLE:

import json

enum JobTitle {
    manager
    executive
    worker
}

struct Employee {
mut:
    name   string
    family string   [json: '-'] // this field will be skipped
    age    int
    salary f32
    title  JobTitle [json: 'ETitle'] // the key for this field will be 'ETitle', not 'title'
}

fn main() {
    x := Employee{'Peter', 'Begins', 28, 95000.5, .worker}
    println(x)
    s := json.encode(x)
    println('JSON encoding of employee x: ${s}')
    assert s == '{"name":"Peter","age":28,"salary":95000.5,"ETitle":"worker"}'
    mut y := json.decode(Employee, s)!
    assert y != x
    assert y.family == ''
    y.family = 'Begins'
    assert y == x
    println(y)
    ss := json.encode(y)
    println('JSON encoding of employee y: ${ss}')
    assert ss == s
}


"""MODULEEND



"""MODULE core.crystaljson
fn json_dict_filter_any(r string, clean bool, include []string, exclude []string) !map[string]json2.Any
get dict out of json if include used (not empty, then will only match on keys given)

fn json_dict_filter_string(r string, clean bool, include []string, exclude []string) !map[string]string
returns a map (dict)

fn json_dict_get_any(r string, clean bool, key string) !json2.Any
get dict out of json if include used (not empty, then will only match on keys given)

fn json_dict_get_string(r string, clean bool, key string) !string

fn json_list(r string, clean bool) []string
rought splitter for json, splits a list of dicts into the text blocks
"""MODULEEND

