brew install ffmpeg
pip3 install git+https://github.com/openai/whisper.git
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
make base.en
bash ./models/download-ggml-model.sh base.en
ffmpeg -f avfoundation -i ":0"  -ar 16000 -ac 1 -c:a pcm_s16le audiocapture.wav ; open audiocapture.wav
# ffmpeg -f avfoundation -list_devices true -i ""