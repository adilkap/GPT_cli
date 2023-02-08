import os
import sys
import openai
import wandb
from pprint import pprint 

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_prompt = str(sys.argv[1])
MAX_TOKENS = 2500

response = openai.Completion.create(
	engine="text-davinci-002",
  	prompt=gpt_prompt,
  	temperature=0.5,
  	max_tokens=MAX_TOKENS,
  	top_p=1.0,
  	frequency_penalty=0.0,
  	presence_penalty=0.0
)

responseText = response['choices'][0]['text']
length = len(responseText)
print(f"This is the response: {length} tokens received")
print(responseText)
print("\n\n")
