set -ex

export AIHOME=~/.virtualenvs/ai

# rm -rf $AIHOME

# pip3 install pew
pew new ai -d 
# pew in ai pip3 install langchain openai ipython wikipedia PyPDF2 PyCryptodome gradio gpt_index
pew in ai pip3 install langchain openai ipython wikipedia PyPDF2 PyCryptodome gradio llama-index nltk llama_hub protobuf pypdf reportlab pdfplumber
pew in ai pip3 install mypy

pushd $AIHOME

# rm -rf $AIHOME/share
# find $AIHOME -name "*.pyc" -type f -delete
# find $AIHOME -type d -name "*-info" -exec rm -r {} +
# find $AIHOME -type d -name "__pycache__" -exec rm -r {} +

# du -h . | sort -h

# tar -cJvf /tmp/ai.tar.xz .
#14 MB right now

popd

pew workon ai
