git clone git@gitlab.com:famedly/conduit.git
cd conduit
docker build --tag matrixconduit/matrix-conduit:latest .
conduit % docker run -p 5555:6167 \
  -v db2:/var/lib/matrix-conduit/ \
  -e CONDUIT_SERVER_NAME="localhost" \
  -e CONDUIT_DATABASE_BACKEND="rocksdb" \
  -e CONDUIT_ALLOW_REGISTRATION=true \
  -e CONDUIT_ALLOW_FEDERATION=true \
  -e CONDUIT_MAX_REQUEST_SIZE="20000000" \
  -e CONDUIT_TRUSTED_SERVERS="[\"matrix.org\"]" \
  -e CONDUIT_MAX_CONCURRENT_REQUESTS="100" \
  -e CONDUIT_LOG="warn,rocket=off,_=off,sled=off" \
  --name conduit matrixconduit/matrix-conduit:latest