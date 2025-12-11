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
    

# print(generate_response("""You are a career advisor bot. Based on the following answers, suggest **the most suitable profession or up to three options**. Respond only with profession names, separated by commas, no explanations.

# Q1 (Describe your favorite subjects at school): (Math, Computer Science)
# Q2 (Do you prefer working with people, data, or machines?): (Data)
# Q3 (Do you like creative work or structured tasks?): (Structured tasks)
# Q4 (Do you like indoor or outdoor work?): (Indoor)
# Q5 (Do you prefer leadership roles or independent work?): (Independent)"""))


# from huggingface_hub import InferenceClient
# import os
# from dotenv import load_dotenv
# load_dotenv()
# print(os.getenv("AI_API"))
# client = InferenceClient(token=os.getenv("AI_API"),
#                          provider="hf-inference")
# output = client.text_generation(
#     model="zai-org/GLM-4.5", 
#     prompt="Explain what is a neural network in simple terms."
# )
# print(output)
# import httpx

# try:
#     r = httpx.get("https://huggingface.co")
#     print("Success!", r.status_code)
# except Exception as e:
#     print("Error:", e)
# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient()

# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {
#             "role": "user",
#             "content": "How many 'G's in 'huggingface'?"
#         }
#     ],
# )

# print(completion.choices[0].message)

