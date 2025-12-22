import os
from openai import OpenAI
from dotenv import load_dotenv
import httpx
load_dotenv()


def generate_response(prompt:str) -> str:
    try:
        client = OpenAI(
        api_key=os.environ.get("OPENAI_API"),
        base_url="https://api.groq.com/openai/v1",
    )

        response = client.responses.create(
            input=prompt,
            model="openai/gpt-oss-20b",
        )
        return response.output_text
    except (httpx.ConnectError, httpx.ReadTimeout) as e:
        return f'Connection error {e},please try again in a gew seconds.'


#print(generate_response("Hello,can you read this?"))

