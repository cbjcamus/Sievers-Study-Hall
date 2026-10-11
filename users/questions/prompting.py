import os
import json

from huggingface_hub import InferenceClient
from huggingface_hub.errors import BadRequestError

from users.session_management.logging import log_prompt_usage

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


def get_response_from_prompt(unit, exercise, prompt):
    client = InferenceClient(
        api_key=os.environ["HF_TOKEN"],
        provider="groq",
    )

    def make_request():
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
            extra_body={
                "reasoning_effort": "low"
            }
        )

        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        usage= response.usage

        log_prompt_usage(unit, exercise, input_tokens, output_tokens, usage)

        return json.loads(response.choices[0].message.content)

    try:
        return make_request()

    except BadRequestError as e:
        if "json_validate_failed" not in str(e):
            raise

        # Retry once
        try:
            return make_request()

        except BadRequestError as retry_error:
            if "json_validate_failed" not in str(retry_error):
                raise

            return None
