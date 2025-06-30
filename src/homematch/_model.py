import os
from typing import Any

from langchain_openai import OpenAI
from openai import OpenAI as OpenAIClient

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-nano")


class Model(OpenAI):
    client: Any = OpenAIClient(
        base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY
    ).completions
    model: str = OPENAI_MODEL
