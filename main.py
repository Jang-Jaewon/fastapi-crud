from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


@app.post("/items", status_code=201)
async def crate_item(name: str):
    return {"name": name}


@app.delete("/items/{[pk}", status_code=204)
async def delete_item(pk: str):
    print("pk", pk)
    return


@app.get("/items", status_code=401)
async def read_items_redirect():
    return {"hello": "world"}
