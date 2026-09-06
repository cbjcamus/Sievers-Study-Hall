import os
import json

from huggingface_hub import InferenceClient

def get_response_from_prompt(prompt):
    client = InferenceClient(
        api_key=os.environ["HF_TOKEN"],
        provider="auto",
    )

    response = client.chat.completions.create(
        model="Qwen/Qwen3-235B-A22B-Instruct-2507",
        messages=[
            {
                "role": "user",
                "content": "/no_think\n" + prompt,
            }
        ],
        temperature=0.7,
        max_tokens=300,
    )

    response = response.choices[0].message.content
    response = json.loads(response)

    print(response)
    print(type(response))

    return response

