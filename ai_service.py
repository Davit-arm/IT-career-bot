import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import httpx
load_dotenv()
def generate_response(prompt: str) -> str:
    try:
        client = InferenceClient(
            api_key=os.getenv("AI_API")
        )
        completion = client.chat.completions.create(
            model="zai-org/GLM-4.5:nebius",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )
        return completion.choices[0].message["content"]
    except (httpx.ConnectError, httpx.ReadTimeout) as e:
        print(f"Netork error {e}")
        return "Connection Error, please try again in a few seconds."
    



