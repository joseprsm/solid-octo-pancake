import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

from homematch.utils import generate_random_string

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    OPENAI_API_KEY = generate_random_string()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY  # yes. this is required.

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "granite-embedding")
CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen3:4b")

_client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)

model = ChatOpenAI(model=CHAT_MODEL, client=_client.chat.completions)

embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    client=_client.embeddings,
    check_embedding_ctx_length="localhost" not in OPENAI_API_BASE,
)
