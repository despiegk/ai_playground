# go install github.com/fiatjaf/noscl@latest
export PATH=$PATH:~/go/bin
# noscl relay add localhost
noscl relay add ws://localhost:7447
noscl setprivate 792ee16b05b2ce728b2d6284565f5c5245c37b475f5398274eed610eb45b65e4
noscl publish test
