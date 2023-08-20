import json
import os
from pprint import pprint
 
import bitsandbytes as bnb
import pandas as pd
import torch
import torch.nn as nn
import transformers
from datasets import load_dataset
from huggingface_hub import notebook_login
from peft import (
    LoraConfig,
    PeftConfig,
    PeftModel,
    get_peft_model,
    prepare_model_for_kbit_training,
)
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
 
#this is the additional data we will load
with open("ecommerce-faq.json") as json_file:
    data = json.load(json_file)

MODEL_NAME = "tiiuae/falcon-7b"
 
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
 
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=bnb_config,
)
 
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token



model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["query_key_value"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
 
model = get_peft_model(model, config)
# print_trainable_parameters(model)

prompt = f"""
<human>: How can I create an account?
<assistant>:
""".strip()
print(prompt)

generation_config = model.generation_config
generation_config.max_new_tokens = 200
generation_config.temperature = 0.7
generation_config.top_p = 0.7
generation_config.num_return_sequences = 1
generation_config.pad_token_id = tokenizer.eos_token_id
generation_config.eos_token_id = tokenizer.eos_token_id
# generation_config

device = "cuda:0"
 
encoding = tokenizer(prompt, return_tensors="pt").to(device)
with torch.inference_mode():
    outputs = model.generate(
        input_ids=encoding.input_ids,
        attention_mask=encoding.attention_mask,
        generation_config=generation_config,
    )
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

data = load_dataset("json", data_files="dataset.json")

def generate_prompt(data_point):
    pprint(data_point)
    if "question" in data_point:
        return f"""
<human>: {data_point["question"]}
<assistant>: {data_point["answer"]}
""".strip()
    else:
        return f"""
<human>: question 1
<assistant>: nothing
""".strip()

 
 
def generate_and_tokenize_prompt(data_point):
    full_prompt = generate_prompt(data_point)
    tokenized_full_prompt = tokenizer(full_prompt, padding=True, truncation=True)
    return tokenized_full_prompt
 
data2 = data["train"].shuffle().map(generate_and_tokenize_prompt)
data2


#https://www.mlexpert.io/prompt-engineering/fine-tuning-llm-on-custom-dataset-with-qlora#user-content-fn-8