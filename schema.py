from typing import Optional, List

from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str = Field(..., pattern="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$")
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="The description of the item", max_length=100)
    price: float = Field(..., gt=0, description="The price must be greater than zero.")
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class Importance(BaseModel):
    importance: int
