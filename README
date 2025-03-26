# Intro
This project is a terminal chatbot that user can communicate with the GPT models through OPENAI api

## Features
The main feature of this project is not the chatbot itself it's the prompt engineering feature that
optimizes the bot the retrieve the best result possbile from typical users that have no Prompt
Engineering knowledge

The chatbot encourages itself to ask user different questions based on the user input for example:

1. If the user input is simple the bot will asnwer their questions directly with **Zero-Shot** technique
2. If the user input needs minimum amount of information the bot will encourage the user to provide
   more information encouraging **One-Shot** technique
3. If the user asks complicated question the bot will encourage the user to provide more examples
   for optimized **Chain Of Thought** and **Few-Shot** technique

## Setup
Create a `.env` file in root of your project using `env-example.txt` that will provide a valid
sample then run the `main.py` file.

> [!Warning]
> This Project is based on Metis Platform wrapper api if you are not willing/able to use it
> you can use the OPENAI API with a simple manipulation and a single env key: ` OPENAI_API_KEY="your_api_key_here"`

### OPENAI API

If you want to use OPENAI this the base code for input and output:

main.py
```
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)
```

.env

```
OPENAI_API_KEY="your_api_key_here"
```
