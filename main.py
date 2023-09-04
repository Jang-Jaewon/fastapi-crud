from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Optional, Literal
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import Image, Importance, Item, Offer, User, UserBase, UserIn, UserOut

app = FastAPI()


items = {
    "Foo": {
        "name": "Foo", "price": 50.2
    },
    "Bar": {
        "name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2
    },
    "Baz": {
        "name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []
    }
}


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item


@app.post("/items{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["Foo", "Bar", "Baz"]):
    return items[item_id]


@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    return user

