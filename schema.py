from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


class Importance(BaseModel):
    importance: int


class UserBase(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: bool | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


class ListItem(BaseModel):
    name: str
    description: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool = False


class UserInDB(User):
    hashed_password: str
