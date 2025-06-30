import json

import click

from homematch.gen import generate_listings, generate_neighborhoods
from homematch.schemas import Listing, Neighborhoods


@click.group
def cli():
    pass


@cli.command()
@click.option(
    "--n-neighborhoods", default=3, help="Number of neighborhoods to generate"
)
@click.option("--n-quirks", default=3, help="Number of quirks per neighborhood")
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
    default=3,
    help="Minimum number of listings to generate per neighborhood",
)
@click.option(
    "--max-listings",
    "--max",
    default=7,
    help="Maximum number of listings to generate per neighborhood",
)
def generate(
    n_neighborhoods: int = 3,
    n_quirks: int = 3,
    k: int = None,
    output: str = "data/listings.jsonl",
    min_listings: int = 3,
    max_listings: int = 7,
):
    neighborhoods: Neighborhoods = generate_neighborhoods(
        k=n_neighborhoods, n_quirks=n_quirks
    )
    listings: list[Listing] = []
    for neighborhood in neighborhoods.root:
        listings += generate_listings(
            neighborhood_name=neighborhood.name,
            neighbor_description=neighborhood.description,
            neighborhood_quirks=neighborhood.quirks,
            k=k,
            min_listings=min_listings,
            max_listings=max_listings,
        ).root

    with open(output, "w") as f:
        for listing in listings:
            f.write(json.dumps(listing.model_dump(mode="json")) + "\n")
