import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(".secrets")

client = OpenAI(
    api_key="any",
    base_url="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    default_headers={
        "x-api-key": os.getenv("API_GATEWAY_KEY")
    }
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)
