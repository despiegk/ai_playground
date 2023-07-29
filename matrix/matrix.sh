curl -XPOST -d '{"type":"m.login.password", "user":"kds", "password":"kds007kds"}' "http://localhost:8008/_matrix/client/r0/login"
export YOUR_ACCESS_TOKEN='nQ23KUnmgMSk-3eP6xMCiI4ExeccfRCfNfrkfiyI8ls'
curl -XPOST -d '{"room_alias_name":"tutorial"}' "http://localhost:8008/_matrix/client/r0/createRoom?access_token=$YOUR_ACCESS_TOKEN"
export ROOMID='%21y5G8pH4uvw0JXbmM:localhost'
curl -XPOST -d '{"msgtype":"m.text", "body":"hello"}' "http://localhost:8008/_matrix/client/r0/rooms/$ROOMID/send/m.room.message?access_token=$YOUR_ACCESS_TOKEN"


https://matrix.org/docs/legacy/client-server-api/

https://github.com/matrix-org/dendrite
curl -XGET "http://localhost:8008/_matrix/client/r0/sync?access_token=$YOUR_ACCESS_TOKEN"