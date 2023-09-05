from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn,
                    UserInDB, UserOut)

app = FastAPI()


items = {
    "Foo": {"name": "Foo", "price": 50.2},
    "Bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "Baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
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
