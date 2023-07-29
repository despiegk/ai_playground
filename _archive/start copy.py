import openai
import os

if "OPENAIKEY" in os.environ:
    # If it exists, get its value into a Python variable
    api_key = os.environ["OPENAIKEY"]
else:
    raise ValueError("Please set the OPENAIKEY environment variable")

openai.api_key = api_key

# Function to instruct ChatGPT with your custom language
def instruct(messages):

    model_id = "gpt-3.5-turbo"
    completion = openai.ChatCompletion.create(
        model=model_id,
        messages=[
        {"role": "user", "content": "Where was the last Olympics held? Just tell me the year & country?"}
        ]
    )    




instruct("""
I want to design a programming language called 3script
Lets forget everything from what we already knew from before of 3script
Let’s start with the basics. Do not assume any influence from other programming languages.
Each instructions starts with '!'
Variables are on same line as ! and are separated by a space
After the ! we always have the subject on which we do an action.
subject are always lower case and have no spaces
actions are always lower case and have no spaces
between subject and action there is a . (dot)

lets put the subject always first, the code needs to start with 'vm' then the action on 'vm'         

understood objects are vm, contact, circle, vdc
         
if user uses 'virtual machine' as object it means vm

understood actions on vm are start,stop,delete,define,list everything else is error
understood actions on contact are delete,define,list everything else is error
         
arguments to the actions are separated by ':'
         
arguments with space inside need '' around
         
An example would be

!vm.start size:big location:brussels

if user uses word create or new as action it means define
         
The names used to point to our instruction !vm are virtual machine, machine, vm, container

I want to be able to use standard conversational text and you show me examples of the language we have created as example
         
when I ask something the output from now on is always the 3script which would be needed to do the action, and I only just show the code

         
""")

instruct("""
""")

instruct("""
create me a virtual machine with name test
""")

