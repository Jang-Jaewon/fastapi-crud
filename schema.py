from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
