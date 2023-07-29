# https://github.com/fiatjaf/relayer/tree/master/examples/basic
export POSTGRESQL_DATABASE=postgres://postgres:1234@localhost:5432/nostr?sslmode=disable
go install github.com/fiatjaf/relayer/basic@latest
go install github.com/fiatjaf/noscl@latest
export PATH=$PATH:~/go/bin
basic