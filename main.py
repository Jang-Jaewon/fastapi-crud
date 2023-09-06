from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


items = {
    "item1": {"description": "this is description hello", "type": "car"},
    "item2": {
        "description": "Music is my dog, it my icecream",
        "type": "plane",
        "size": 5
    },
}


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User 'saved'.")
    return user_in_db


@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]


list_items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"}
]


@app.get("/list_items/", response_model=list[ListItem])
async def read_items():
    return items


@app.get("/arbitrary", response_model=dict[str, float])
async def get_arbitrary():
    return {"foo":1, "bar": 2}
