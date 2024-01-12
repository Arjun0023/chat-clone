#!/usr/bin/env python3
# Import modules
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Use your own api
openai.api_key = os.getenv('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')

# Set up the model and prompt
model_engine = "text-davinci-003"

# Set response until otherwise cancelled
prompt = input("🤖 How can I help you?\n")

while prompt.lower() not in ("no", "n", "no!", "you can't", "you cant", "nothing"):
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(f'🤖 {response}')
    
    prompt = input("🤖 What else can I help you with?\n")

print("🤖...")
