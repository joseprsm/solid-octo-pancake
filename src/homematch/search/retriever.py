from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers import SelfQueryRetriever
from langchain.vectorstores import VectorStore

from homematch import model


def get_retriever(store: VectorStore):
    metadata_field_info = [
        AttributeInfo(
            name="price",
            description="The price of the listing in EUR",
            type="number",
        ),
        AttributeInfo(
            name="bedrooms",
            description="The number of bedrooms in the listing",
            type="number",
        ),
        AttributeInfo(
            name="bathrooms",
            description="The number of bathrooms in the listing",
            type="number",
        ),
        AttributeInfo(
            name="size",
            description="The size of the listing in squared meters",
            type="number",
        ),
        AttributeInfo(
            name="neighborhood",
            description="The name of the neighborhood where the listing is located",
            type="string",
        ),
    ]

    return SelfQueryRetriever.from_llm(
        model,
        store,
        document_contents="Description of a real estate listing and its neighborhood",
        metadata_field_info=metadata_field_info,
    )
