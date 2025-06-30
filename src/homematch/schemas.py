import os

from pydantic import BaseModel, Field

from homematch.utils import load_jsonl, write_jsonl


class _BaseList(BaseModel):
    root: list

    def __iter__(self):
        return iter(self.root)

    def __len__(self):
        return len(self.root)

    def __getitem__(self, index: int):
        return self.root[index]

    def __add__(self, other: "_BaseList") -> "_BaseList":
        if isinstance(other, list):
            other = _BaseList(root=other)
        return _BaseList(root=self.root + other.root)


class Neighborhood(BaseModel):
    name: str = Field(description="The name of the neighborhood")
    description: str = Field(description="A brief description of the neighborhood")
    quirks: list[str] = Field(
        description="Unique characteristics or quirks of the neighborhood"
    )


class Neighborhoods(_BaseList):
    root: list[Neighborhood] = Field(
        default=[],
        description="A list of neighborhoods, each with a name, description, and unique quirks",
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
    neighborhood_description: str = Field(
        description="A brief description of the neighborhood where the listing is located"
    )


class Listings(_BaseList):
    root: list[Listing] = Field(
        default=[],
        description="A list of real estate listings, each with a description, price, number of bedrooms, bathrooms, and size",
    )

    @classmethod
    def load(cls, file_path: str) -> "Listings":
        listings = load_jsonl(file_path)
        return cls(root=listings)

    def write(self, file_path: str):
        listings: list[dict] = self.model_dump(mode="json")["root"]
        write_jsonl(file_path, listings)
