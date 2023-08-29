from enum import Enum
from typing import Optional

from fastapi import FastAPI, Path, Query, Body

from schema import Item, User, Importance

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item
):
    result = {"item_id": item_id, "item": item}
    return result
