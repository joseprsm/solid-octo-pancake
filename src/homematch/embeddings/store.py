import json

from langchain_chroma import Chroma
from langchain_core.documents import Document

from homematch import METADATA_FIELDS, TEXT_FIELDS, Embeddings
from homematch.schemas import Listing


def convert_to_document(listing: Listing) -> Document:
    def get_data(obj, fields):
        return {field: obj[field] for field in fields if field in obj}

    page_content = get_data(listing, TEXT_FIELDS)
    metadata = get_data(listing, METADATA_FIELDS)
    return Document(page_content=json.dumps(page_content), metadata=metadata)


def construct_vector_store(
    collection_name: str = "listings", persist_directory: str = "./chroma"
) -> None:
    return Chroma(
        embedding_function=Embeddings(),
        persist_directory=persist_directory,
        collection_name=collection_name,
    )
