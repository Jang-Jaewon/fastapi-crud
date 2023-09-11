from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         None, title="The description of the item", max_length=100
#     )
#     price: float = 10.5
#     tax: float | None = None
#     tag: list[str] = []

class Item(BaseModel):
    title: str
    size: int


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


class User(BaseModel):
    username: str
    password: str


class Importance(BaseModel):
    importance: int


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


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
