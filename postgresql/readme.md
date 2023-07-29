quickly get ourselves a postgresql

## how to get inside docker

```bash
docker exec -it basic-postgres /bin/sh
```

## how to connect over client to it

```bash
export PGPASSWORD=1234
psql --username postgres -h localhost
```

## create DB

go into psql then do 
```bash
CREATE DATABASE mydb;
```



