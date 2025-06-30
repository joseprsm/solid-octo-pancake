import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-nano")


class LLM(ChatOpenAI):
    openai_api_base: str = OPENAI_API_BASE
    api_key: str = OPENAI_API_KEY
    model: str = CHAT_MODEL


class Embeddings(OpenAIEmbeddings):
    openai_api_base: str = OPENAI_API_BASE
    api_key: str = OPENAI_API_KEY
    model: str = "text-embedding-3-small"
