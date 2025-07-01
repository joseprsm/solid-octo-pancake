import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

from homematch.utils import generate_random_string

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    OPENAI_API_KEY = generate_random_string()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1")
elif OPENAI_API_KEY.startswith("voc-"):
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
else:
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "granite-embedding")
CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen3:4b")


model = ChatOpenAI(
    model=CHAT_MODEL, api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE
)  # cannot be using the client, as it's trying to fetch .root_client


embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    client=OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE).embeddings,
    check_embedding_ctx_length="localhost" not in OPENAI_API_BASE,
)
