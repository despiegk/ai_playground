import openai
import os
from pprint import pprint; import IPython
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.cache import SQLiteCache

import langchain

def read_text_files(directory_path):
    files_text = []
    
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), "r") as file:
                files_text.append(file.read())
    
    return files_text

def text_to_ascii(input_text:str) -> str:
    ascii_text = ''
    for character in input_text:
        ascii_text += str(ord(character)) + ' '
    return ascii_text.rstrip()  # remove trailing space

# Check if the environment variable exists
if "OPENAIKEY" in os.environ:
    # If it exists, get its value into a Python variable
    api_key = os.environ["OPENAIKEY"]
else:
    raise ValueError("Please set the OPENAIKEY environment variable")

openai.api_key = api_key


llm = OpenAI(openai_api_key=api_key)
chat_model = ChatOpenAI(openai_api_key=api_key)


langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

llm.predict("Tell me a joke")
llm.predict("Tell me a joke")

IPython.embed()
