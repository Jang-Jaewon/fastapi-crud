from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import (Body, Cookie, FastAPI, File, Form, Header, HTTPException,
                     Path, Query, Request, UploadFile, status, Depends)
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (http_exception_handler,
                                        request_validation_exception_handler)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, User, UserBase, UserIn, UserInDB, UserOut)

app = FastAPI()


async def hello():
    return "world"


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100, blah: str = Depends(hello)):
    return {"q": q, "skip": skip, "limit": limit, "hello": blah}

@app.get("/items")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
