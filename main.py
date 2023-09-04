from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Optional
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import Image, Importance, Item, Offer, User

app = FastAPI()


@app.get("/items")
async def read_items(
    cookie_id: str | None = Cookie(None),
    accept_encoding: str | None = Header(None),
    user_agent: str | None = Header(None),
    x_token: list[str] | None = Header(None),
):
    return {
        "cookie_id:": cookie_id,
        "Accept_Encoding": accept_encoding,
        "User_Agent": user_agent,
        "X_Token": x_token,
    }
