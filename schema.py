from typing import Optional, List

from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="The description of the item", max_length=100)
    price: float = Field(..., gt=0, description="The price must be greater than zero.")
    tax: float | None = None
    tags: List[int] = []


class User(BaseModel):
    username: str
    full_name: str | None = None


class Importance(BaseModel):
    importance: int
