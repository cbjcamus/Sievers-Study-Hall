import os
import json

from huggingface_hub import InferenceClient

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "exercise_feedback",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "inquiry_correct": {
                    "type": "string",
                    "enum": ["yes", "no"]
                },
                "meaning_coherent": {
                    "type": "string",
                    "enum": ["yes", "no"]
                },
                "german_sentence": {
                    "type": "string"
                },
                "translation": {
                    "type": "string"
                },
                "commentary": {
                    "type": "string"
                }
            },
            "required": [
                "inquiry_correct",
                "meaning_coherent",
                "german_sentence",
                "translation",
                "commentary"
            ],
            "additionalProperties": False
        }
    }
}


def get_response_from_prompt(prompt):
    client = InferenceClient(
        api_key=os.environ["HF_TOKEN"],
        provider="groq",
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.7,
        max_tokens=500,
        response_format=response_format,
        extra_body = {
            "reasoning_effort": "low"
        }
    )

    message = response.choices[0].message

    response_dict = json.loads(message.content)

    return response_dict
