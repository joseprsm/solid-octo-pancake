import os

import click

from homematch.embeddings.store import VectorStore
from homematch.generate import generate_listings, generate_neighborhoods
from homematch.schemas import Listings, Neighborhoods


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
def search():
    """Search for listings in the vector store."""
    vector_store = VectorStore()

    print("Enter your search query (or 'exit' to quit):")
    while True:
        query = input("> ")
        if query.lower() == "exit":
            break
        results = vector_store.search(query)
        for result in results:
            print(result)


if __name__ == "__main__":
    cli()
