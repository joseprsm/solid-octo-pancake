import os

from pydantic import BaseModel, Field


class Neighborhood(BaseModel):
    name: str = Field(description="The name of the neighborhood")
    description: str = Field(description="A brief description of the neighborhood")
    quirks: list[str] = Field(
        description="Unique characteristics or quirks of the neighborhood"
    )


class Neighborhoods(BaseModel):
    root: list[Neighborhood] = Field(
        description="A list of neighborhoods, each with a name, description, and unique quirks"
    )


class Listing(BaseModel):
    description: str = Field(description="A description of the real estate listing")
    price: int = Field(
        description=f"The price of the listing in {os.environ.get('CURRENCY', 'EUR')}"
    )
    bedrooms: int = Field(description="The number of bedrooms in the listing")
    bathrooms: int = Field(description="The number of bathrooms in the listing")
    size: int = Field(
        description=f"The size of the listing in squared {os.environ.get('SIZE_UNIT', 'meters')}"
    )
    neighborhood: str = Field(
        description="The name of the neighborhood where the listing is located"
    )


class Listings(BaseModel):
    root: list[Listing] = Field(
        description="A list of real estate listings, each with a description, price, number of bedrooms, bathrooms, and size"
    )
