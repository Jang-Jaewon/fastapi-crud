from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import (Body, Cookie, Depends, FastAPI, File, Form, Header,
                     HTTPException, Path, Query, Request, UploadFile, status)
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (http_exception_handler,
                                        request_validation_exception_handler)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, User, UserBase, UserIn, UserInDB, UserOut)
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token):
    return User(
        username=f"{token} fake decode",
        email="foo@example.com",
        full_name="Foo bar"
    )


async def get_current_user(token: str = Depends(oauth2_schema)):
    user = fake_decode_token(token)
    return user


@app.get("/user/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/items")
async def read_items(token: str = Depends(oauth2_schema)):
    return {"token": token}
