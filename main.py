from enum import Enum
from typing import Optional, List

from fastapi import FastAPI, Path, Query, Body

from schema import Item, User, Importance, Offer, Image

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
