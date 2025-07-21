import json
import os
from datetime import datetime

import click
from langchain_core.documents import Document

from homematch.embeddings.store import VectorStore
from homematch.generate import generate_listings, generate_neighborhoods
from homematch.schemas import Listings, Neighborhoods, SearchQuestion
from homematch.search.chat import get_user_preferences, rank, summarise
from homematch.search.retriever import get_retriever


@click.group
def cli():
    pass


@cli.command()
@click.option(
    "--neighborhoods",
    "-n",
    "n_neighborhoods",
    default=3,
    help="Number of neighborhoods to generate",
)
@click.option(
    "--quirks", "-q", "n_quirks", default=3, help="Number of quirks per neighborhood"
)
@click.option(
    "--k",
    type=int,
    default=None,
    help="Number of listings to generate per neighborhood",
)
@click.option(
    "--output", default="data/listings.jsonl", help="Output file for generated listings"
)
@click.option(
    "--min-listings",
    "--min",
    "-m",
    default=3,
    help="Minimum number of listings to generate per neighborhood",
)
@click.option(
    "--max-listings",
    "--max",
    "-M",
    default=7,
    help="Maximum number of listings to generate per neighborhood",
)
def generate(
    n_neighborhoods: int = 3,
    n_quirks: int = 3,
    k: int = None,
    output: str = os.path.join("data", "listings.jsonl"),
    min_listings: int = 3,
    max_listings: int = 7,
):
    neighborhoods: Neighborhoods = generate_neighborhoods(
        k=n_neighborhoods, n_quirks=n_quirks
    )
    listings = Listings()
    for neighborhood in neighborhoods:
        listings += generate_listings(
            neighborhood_name=neighborhood.name,
            neighbor_description=neighborhood.description,
            neighborhood_quirks=neighborhood.quirks,
            k=k,
            min_listings=min_listings,
            max_listings=max_listings,
        )

    listings.write(output)


@cli.command
@click.option(
    "--inputs", default="data/listings.jsonl", help="Input file with listings"
)
@click.option("--colection-name", "--collection", "collection_name", default="listings")
@click.option("--persist-directory", "--directory", default="./chroma")
def embeddings(
    inputs: str = "data/listings.jsonl",
    collection_name: str = "listings",
    persist_directory: str = "./chroma",
):
    listings = Listings.load(inputs)
    vector_store = VectorStore(
        collection_name=collection_name, persist_directory=persist_directory
    )
    vector_store.add_listings(listings)


@cli.command
@click.option(
    "--output",
    "-o",
    default=None,
    help="Output file for search results (default: search_results.txt)",
)
def search(output: str = None):
    """Search for listings in the vector store."""
    messages = []
    vector_store = VectorStore(collection_name="listings", persist_directory="./chroma")
    retriever = get_retriever(vector_store)

    result: SearchQuestion = get_user_preferences(conversation=messages)
    while True:
        print(f"🤖 {result.question}")
        msg = input("> ")
        if msg == "/bye" or msg == "":
            break
        result.answer = msg
        messages.append(result.model_dump())
        result = get_user_preferences(conversation=messages)

    query: str = summarise(messages).content

    print(f"\nSearching for listings matching: {query}\n")
    results: list[Document] = retriever.invoke(query)

    # Save raw search results to JSONL file
    results_file = (
        f"raw_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    )
    with open(results_file, "w", encoding="utf-8") as f:
        # Write query as first line
        f.write(
            json.dumps({"query": query, "timestamp": datetime.now().isoformat()}) + "\n"
        )

        # Write each result as a separate JSON line
        for doc in results:
            result_data = {"page_content": doc.page_content, "metadata": doc.metadata}
            f.write(json.dumps(result_data) + "\n")

    print(f"Raw search results saved to {results_file}")

    res = rank(query, results)
    print("\nRanked Listings:")

    output_file = (
        output or f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("HomeMatch Search Results\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Search Query: {query}\n")
        f.write("-" * 60 + "\n\n")

        for i, listing in enumerate(res, 1):
            f.write(f"{i}. {listing.title}\n")
            f.write(f"   Score: {listing.score:.2f}/10\n")
            f.write(f"   Description: {listing.description}\n")
            f.write("-" * 50 + "\n\n")

    print(f"\nSearch results saved to {output_file}")

    # Also print the results to console
    for i, listing in enumerate(res.root, 1):
        print(f"{i}. {listing.title}")
        print(f"   Score: {listing.score:.2f}")
        print(f"   Description: {listing.description}")
        print("-" * 40)


if __name__ == "__main__":
    cli()
