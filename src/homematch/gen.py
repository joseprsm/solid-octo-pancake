from random import randint

from homematch import model
from homematch.schemas import Listings, Neighborhoods


def generate_neighborhoods(k: int = 3, n_quirks: int = 3) -> Neighborhoods:
    prompt = (
        'You\'re generating {k} neighborhoods for a fictional town. Each of the neighborhoods should be a bit "off", but otherwise extremely liveable.'
        "Each neighborhood should have a unique name, a description, and a list of unique characteristics or quirks. "
        "The description should be a few sentences long, and make the neighborhood sound appealing."
        "Generate at list {n_quirks} quirks for each neighborhood. "
        "Be as quirky and creative as possible."
        "Make them silly."
    )
    return model.with_structured_output(Neighborhoods).invoke(
        prompt.format(k=k, n_quirks=n_quirks)
    )


def generate_listings(
    neighborhood_name: str,
    neighbor_description: str,
    neighborhood_quirks: list[str],
    k: int = None,
    min_listings: int = 4,
    max_listings: int = 7,
):
    prompt = (
        "You're generating {k} real estate listings for a fictional town. "
        "The listing is in the {neighborhood} neighborhood. "
        "This is the description of the neighborhood: \n{description}\n "
        "The neighborhood has the following unique characteristics or quirks: \n {quirks}\n "
        "Write in a warm, inviting tone suitable for real estate buyers. The description should highlight attractive features and evoke a strong sense of place."
        "Make up features for the listings that are consistent with the neighborhood quirks. Don't be afraid of being a bit silly. "
        "Include at least one of the neighborhood quirks in each listing. "
        "Always make up something unique about the listing."
        "The description should a few sentences long. "
        "Be as quirky and creative as possible."
    )
    return model.with_structured_output(Listings).invoke(
        prompt.format(
            k=k or randint(min_listings, max_listings),
            neighborhood=neighborhood_name,
            description=neighbor_description,
            quirks="; -".join(neighborhood_quirks),
        )
    )
