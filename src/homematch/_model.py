import os

from langchain_openai import OpenAI

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-nano")


class Model(OpenAI):
    openai_api_base: str = OPENAI_API_BASE
    api_key: str = OPENAI_API_KEY
    model: str = OPENAI_MODEL
