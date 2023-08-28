from enum import Enum
from typing import Optional

from fastapi import FastAPI, Path, Query, Body

from schema import Item, User, Importance

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
    q: str | None = None,
    item: Item = Body(..., embed=True),  # {item={}}
    # item: Item = Body(...)
    # user: User,
    # importance: int = Body(...)
):
    result = {"item_id": item_id}
    if q:
        result.update({q: q})
    if item:
        result.update({"item": item})
    # if user:
    #     result.update({"user": user})
    # if importance:
    #     result.update({"importance": importance})
    return result
