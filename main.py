from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import (Body, Cookie, FastAPI, File, Form, Header, HTTPException,
                     Path, Query, Request, UploadFile, status)
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (http_exception_handler,
                                        request_validation_exception_handler)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, User, UserBase, UserIn, UserInDB, UserOut)

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    summary="Create an Item",
    description="Create an item with all the information: name; description; price; tax; and a set of",
)
async def create_item(item: Item):
    return item


@app.get("/items", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users", tags=[Tags.users])
async def read_users():
    return [{"username": "PhoebeBuffay"}]
