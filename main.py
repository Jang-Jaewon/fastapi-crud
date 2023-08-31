from enum import Enum
from typing import List, Optional

from fastapi import Body, FastAPI, Path, Query

from schema import Image, Importance, Item, Offer, User

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nic Item",
            "price": "16.25",
            "tax": "1.67",
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
