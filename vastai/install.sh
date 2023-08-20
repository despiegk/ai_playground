set -ex

cd /root
apt install pip -y
pip install  bitsandbytes==0.39.0 
pip install  torch==2.0.1 
pip install  -U git+https://github.com/huggingface/transformers.git@e03a9cc 
pip install  -U git+https://github.com/huggingface/peft.git@42a184f 
pip install  -U git+https://github.com/huggingface/accelerate.git@c9fbb71 
pip install  datasets==2.12.0 
pip install  loralib==0.1.1 
pip install  einops==0.6.1 
pip install  gdown
pip install scipy
pip install ipython

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/include
python3 -m bitsandbytes

gdown 1u85RQZdRTmpjGKcCc5anCMAHZ-um4DUC
cp ecommerce-faq.json dataset.json

# export BNB_CUDA_VERSION=122
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:

