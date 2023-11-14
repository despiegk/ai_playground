


we hope that you can use above code example to learn how to generate Vlang code which calls a rest server over http using the json and httpclient as shown before.

we want to show you how a vlang client needs to be generated based on openapi spec

no reason to return anything, its just for you to learn. 


when we see golang we mean vlang

in openapi spec we see

```json
 "paths": {
        "/pets": {
            "get": {
                "summary": "List all pets",
                "operationId": "listPets",
                "tags": [
                    "pets"
                ],
                "parameters": [
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "How many items to return at one time (max 100)",
                        "required": false,
                        "schema": {
                            "type": "integer",
                            "maximum": 100,
                            "format": "int32"
                        }
                    }
                ],
```

this defines how to call the http client and use above part of the spec

```golang

import freeflowuniverse.crystallib.clients.httpconnection
import json

pub struct MyClient{
pub mut:
	name string
	url string
	connection &httpconnection.HTTPConnection
}

[params]
pub struct MyClientArgs{
pub mut:
	name string
	url string
}


pub fn client_new(args MyClientArgs) ! {
	// http.CommonHeader.authorization: 'Bearer $h.auth.auth_token'

	mut conn := httpconnection.new(name: args.name, url: args.url)!
	
	// do the cache on the connection
	conn.cache.expire_after = 3600 // make the cache expire_after 1h
	// make sure we empty cache
	conn.cache_drop()!

}


[params]
pub struct PetsListArgs{
pub mut:
	limit int
}


pub struct Pet{
pub mut:
    id i64 [required]
    name string [required]
    tag string
}

pub fn pets_list(args PetsListArgs) ![]Pet {
	mut connection := httpconnection.new(name: args.name, url: args.url)!

	//make mutable inside, this allows to change the request where needed
	
	dict_args:=map[string]string{}
	dict_args:={
		limit:args.limit
	}

	mut result:=[]Pet{}

	petlistjson:=connection.get_json_list(prefix:"pets",params:dict_args)!
	for petjson in petlistjson{
		mut pet:=json.decode(Pet,petjson)!
		result<<pet
	}
	
	return result
	
}


```

the Pet returned where defined in the openapi specs as follows

```json
 "components": {
            "schemas": {
                "Pet": {
                    "type": "object",
                    "required": [
                        "id",
                        "name"
                    ],
                    "properties": {
                        "id": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "name": {
                            "type": "string"
                        },
                        "tag": {
                            "type": "string"
                        }
                    }
                },
```

which corresponds to vlang struct

```golang
pub struct Pet{
pub mut:
    id i64 [required]
    name string [required]
    tag string
}

```