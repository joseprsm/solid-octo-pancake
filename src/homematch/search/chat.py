import json

from langchain_core.documents import Document

from homematch import model
from homematch.schemas import RankedListings, SearchQuestion


def get_user_preferences(questions: list[str] = None, conversation: str = None) -> str:
    """Generate a system prompt for asking property preference questions."""
    conversation = conversation or []

    questions = questions or [
        "How big do you want your house to be?",
        "What are 3 most important things for you in choosing this property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?",
    ]

    prompt = (
        "You are a helpful real estate assistant helping users find their perfect home. "
        "Ask the following questions one by one to understand their preferences. "
        "Be conversational and friendly.\n\n"
        "Example questions to ask: \n{questions}\n\n"
        "This is the conversation so far: \n{conversation}\n\n"
        "Only output questions, nothing else."
    )

    prompt = prompt.format(
        conversation=json.dumps(conversation),
        questions="\n  - ".join(questions),
    )

    return model.with_structured_output(SearchQuestion).invoke(prompt)


def summarise(conversation: list[dict[str, str]]):
    prompt = (
        "You are a helpful assistant that summarizes the user's preferences for finding a home. "
        "The user has provided the following information: {conversation}. "
        "Please summarize this information in a single query as concise and clear as you can."
    )

    return model.invoke(prompt.format(conversation=json.dumps(conversation)))


def rank(query: str, results: list[Document]) -> str:
    """Rank the results based on the query."""
    prompt = (
        "You are a helpful assistant that ranks real estate listings based on user preferences. "
        "The user has provided the following query: {query}. "
        "Here are the listings to rank: {results}. "
        "Personalize the listings descriptions to include the query in a natural way, highlihting how they match the user's preferences. "
        "If there's a user preference not mentioned in the listing, do not include it in the description. "
    )

    return model.with_structured_output(RankedListings).invoke(
        prompt.format(
            query=query, results=json.dumps([doc.model_dump() for doc in results])
        )
    )
