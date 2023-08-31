from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        None, title="The description of the item", max_length=100
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero.")
    tax: float | None = None

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "name": "Foo",
    #             "description": "A very nic Item",
    #             "price": "16.25",
    #             "tax": "1.67",
    #         }
    #     }


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
