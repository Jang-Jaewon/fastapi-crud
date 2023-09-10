from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query, status, Form

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


@app.post("/login-form")
async def login_form(username: str = Form(...), password: str = Form(...)):
    print("password", password)
    return {"username": username}


@app.post("/login-json")
async def login_json(username: str = Body(...), password: str = Body(...)):
    print("password", password)
    return {"username": username}
# async def login_json(user: User):
#     return user
