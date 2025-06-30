import json

from langchain_chroma import Chroma
from langchain_core.documents import Document

from homematch import METADATA_FIELDS, TEXT_FIELDS, Embeddings
from homematch.schemas import Listing, Listings


class VectorStore(Chroma):
    def __init__(
        self,
        *,
        collection_name: str,
        embedding_fields: list[str] = None,
        metadata_fields: list[str] = None,
        **kwargs,
    ):
        self.embedding_fields = embedding_fields or TEXT_FIELDS
        self.metadata_fields = metadata_fields or METADATA_FIELDS
        super().__init__(
            embedding_function=Embeddings(), collection_name=collection_name**kwargs
        )

    def add_listing(self, listings: Listings):
        documents = list(map(self._convert_to_document, listings))
        return self.add_documents(documents)

    def _convert_to_document(self, listing: Listing):
        def get_data(obj, fields):
            return {field: obj[field] for field in fields if field in obj}

        page_content = get_data(listing, self.embedding_fields)
        metadata = get_data(listing, self.metadata_fields)
        return Document(page_content=json.dumps(page_content), metadata=metadata)
