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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException as StarletteHTTPException

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, User, UserBase, UserIn, UserInDB, UserOut)

app = FastAPI()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


fake_users_db = {
    "jaewon": dict(
        username="jaewon",
        full_name="Jaewon Jang",
        email="jaewon@example.com",
        hashed_password="fakehashedsecret",
        disable=False,
    ),
    "haezin": dict(
        username="haezin",
        full_name="Haezin Na",
        email="haezin@example.com",
        hashed_password="fakehashedsecret",
        disable=True,
    ),
}


def fake_hash_passwrod(password: str):
    return f"fakehashed{password}"


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    return get_user(fake_users_db, token)


async def get_current_user(token: str = Depends(oauth2_schema)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_activate_user(current_user: User = Depends(get_current_user)):
    if current_user.disable:
        raise HTTPException(
            status_code=400, detail="Inactive user", headers={"WWW-Authent"}
        )
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_passwrod(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/user/me")
async def get_me(current_user: User = Depends(get_current_activate_user)):
    return current_user


@app.get("/items")
async def read_items(token: str = Depends(oauth2_schema)):
    return {"token": token}
