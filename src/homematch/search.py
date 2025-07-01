from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers import SelfQueryRetriever

from homematch import model
from homematch.embeddings.store import VectorStore

SYSTEM_PROMPT = (
    "You are a helpful assistant that helps users find homes based on their preferences. "
    "Begin by asking the user a series of questions to understand their needs, such as preferred location, budget, number of bedrooms, and any specific requirements. "
    "Once you have gathered enough information, use the details to form a human query and return the most relevant listings from the vector store. "
    "The listings are stored in a vector store and you can query them using the search command. "
    "You will return the listings in a JSON format with the following fields: "
    "id, title, description, price, location, and image_url."
)


store = VectorStore(collection_name="listings", persist_directory="./chroma")

documents = store.similarity_search(
    "Find me a house with a large backyard in a quiet neighborhood for less than 500000",
    filter={"price": ""},
)

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


retriever = SelfQueryRetriever.from_llm(
    model,
    store,
    document_contents="Description of a real estate listing and it's neighborhood",
    metadata_field_info=metadata_field_info,
)

retriever.invoke(
    "Find me a house with a large backyard in a quiet neighborhood with more than 1 bathroom for less than 500000 EUR"
)
