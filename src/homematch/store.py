import json

from langchain_chroma import Chroma
from langchain_core.documents import Document

from homematch import METADATA_FIELDS, TEXT_FIELDS, Embeddings
from homematch.schemas import Listing

vector_store = Chroma(
    embedding_function=Embeddings(),
    persist_directory="./chroma",
    collection_name="listings",
)


def convert_to_document(listing: Listing) -> Document:
    def get_data(obj, fields):
        return {field: obj[field] for field in fields if field in obj}

    page_content = get_data(listing, TEXT_FIELDS)
    metadata = get_data(listing, METADATA_FIELDS)
    return Document(page_content=json.dumps(page_content), metadata=metadata)
