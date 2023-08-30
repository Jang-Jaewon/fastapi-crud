from enum import Enum
from typing import Optional, List

from fastapi import FastAPI, Path, Query, Body

from schema import Item, User, Importance, Offer, Image

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item
):
    result = {"item_id": item_id, "item": item}
    return result


@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.post("images/multiple")
async def create_multiple_images(images: list[Image]):
    return images


@app.post("blah")
async def create_some_blahs(blahs: dict[int, float]):
    return blahs