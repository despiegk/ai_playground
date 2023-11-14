set -ex

export MILVUS_HOST=localhost
export MILVUS_PORT=19530
export TOKEN=notimportant

curl http://localhost:9091/healthz

echo 'we will now fetch collections'


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


curl --request GET \
    --url "${MILVUS_HOST}:${MILVUS_PORT}/v1/vector/collections" \
    --header "Authorization: Bearer ${TOKEN}" \
    --header "accept: application/json" \
    --header "content-type: application/json"

