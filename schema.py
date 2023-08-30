from typing import Optional, List

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="The description of the item", max_length=100)
    price: float = Field(..., gt=0, description="The price must be greater than zero.")
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


class User(BaseModel):
    username: str
    full_name: str | None = None


class Importance(BaseModel):
    importance: int
