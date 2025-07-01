import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

from homematch.utils import generate_random_string


def set_env():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = generate_random_string()
        os.environ["OPENAI_API_KEY"] = api_key
        api_base = os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1")
        embedding_model = os.getenv("EMBEDDING_MODEL", "granite-embedding")
        chat_model = os.getenv("CHAT_MODEL", "qwen3:4b")
    else:
        api_base = os.getenv("OPENAI_API_BASE")
        if api_key.startswith("voc-"):
            api_base = os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
        embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        chat_model = os.getenv("CHAT_MODEL", "gpt-4.1-nano")
    return api_key, api_base, embedding_model, chat_model


OPENAI_API_KEY, OPENAI_API_BASE, EMBEDDING_MODEL, CHAT_MODEL = set_env()


model = ChatOpenAI(
    model=CHAT_MODEL, api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE
)  # cannot be using the client, as it's trying to fetch .root_client


embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    client=OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE).embeddings,
    check_embedding_ctx_length="localhost" not in OPENAI_API_BASE,
)
