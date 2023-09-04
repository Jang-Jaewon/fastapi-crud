from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Optional
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import Image, Importance, Item, Offer, User, UserBase, UserIn, UserOut

app = FastAPI()


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item


@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    return user

