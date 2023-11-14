
the following is information about api for vilnus

Create Collection
Creates a collection in a cluster.

POST https://${MILVUS_HOST}:${MILVUS_PORT}/v1/vector/collections/create
Example
Create a collection named medium_articles:

curl --request POST \
     --url "${MILVUS_HOST}:${MILVUS_PORT}/v1/vector/collections/create" \
     --header "Authorization: Bearer ${TOKEN}" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     -d '{
       "dbName": "default",   
       "collectionName": "medium_articles",
       "dimension": 256,
       "metricType": "L2",
       "primaryField": "id",
       "vectorField": "vector"
      }'

Success response:

{
    "code": 200,
    "data": {}
}

Request
Parameters
No query parameters required

No path parameters required

Request Body
{
    "collectionName": "string",
    "dbName": "string",
    "description": "string",
    "dimension": "integer",
    "metricType": "string",
    "primaryField": "string",
    "vectorField": "string"
}

Parameter	Description
dbName	string
The name of the database to which the collection to create belongs to.
collectionName	string(required)
The name of the collection to create.
dimension	integer(required)
The number of dimensions for the vector field of the collection.
The value ranges from 32 to 32768.
metricType	string
The distance metric used for the collection.
The value defaults to L2.
primaryField	string
The primary key field.
The value defaults to id.
vectorField	string
The vector field.
The value defaults to vector.
description	string
The description of the collection
Response
Returns an empty object.

Response Bodies
Response body if we process your request successfully
{
    "code": 200,
    "data": {}
}

Response body if we failed to process your request
{
    "code": integer,
    "message": string
}

Properties
The properties in the returned response are listed in the following table.

Property	Description
code	integer
Indicates whether the request succeeds.
200: The request succeeds.
Others: Some error occurs.
data	object
A data object.
message	string
Indicates the possible reason for the reported error.
Possible Errors
Error Code	Description
800	database not found
1800	user hasn't authenticate
1801	can only accept json format request
1802	missing required parameters
1803	fail to marshal collection schema


can you generate an openapi spec for this

