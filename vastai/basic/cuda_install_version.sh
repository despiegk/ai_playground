
apt install cuda-command-line-tools-12-2 -y
apt install cuda-nvcc-12-2 -y


nvcc --version

watch -n 1 nvidia-smi 