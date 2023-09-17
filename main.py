from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import (Body, Cookie, FastAPI, File, Form, Header, HTTPException,
                     Path, Query, Request, UploadFile, status)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, User, UserBase, UserIn, UserInDB, UserOut)

app = FastAPI()


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["items"])
async def create_item(item: Item):
    return item


@app.get("/items", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users", tags=["users"])
async def read_users():
    return [{"username": "PhoebeBuffay"}]
