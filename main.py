from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query, status

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def crate_item(name: str):
    return {"name": name}


@app.delete("/items/{[pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk: str):
    print("pk", pk)
    return


@app.get("/items", status_code=status.HTTP_302_FOUND)
async def read_items_redirect():
    return {"hello": "world"}
