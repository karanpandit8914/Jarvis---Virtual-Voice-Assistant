from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google CLoud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print (completion.choices[0].message)