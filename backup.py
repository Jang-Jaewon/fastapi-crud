from enum import Enum
from typing import Optional

from fastapi import FastAPI, Path, Query

from schema import Item

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.get("/deprecated", description="deprecated test", deprecated=True)
async def get_deprecated():
    return {"message": "hello from the put route"}


# @app.get("/items")
# async def list_items():
#     return {"message": "list items route"}


# @app.get("/items/{items_id}")
# async def get_item(items_id: int):
#     return {"items_id": items_id}


@app.get("/users")
async def list_users():
    return {"message": "list items route"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }

    return {"food_name": food_name, "message": "i like chocolate milk"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip+limit]


# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat."})
#     return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat."
            }
        )
    return item


# @app.get("/items/{item_id}")
# async def get_item(
#     item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat."
#             }
#         )
#     return item


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_txt = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_txt})
    return item_dict


@app.post("/items{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
# async def read_items(q: str | None = Query(None, min_length=3, max_length=10)):  # Default=None
# async def read_items(q: str | None = Query(..., min_length=3, max_length=10)):  # required & min/max
# async def read_items(q: list[str] | None = Query(["foo", "bar"])):  # items?q=a&q=b&q=c&q=d
async def read_items(
    q: str
    | None = Query(
        None,
        min_length=3,
        max_length=10,
        title="Sample title",
        description="sample description",
        alias="item-query"
        # deprecated=True,
    )
):  # item?item-query="foo"
    result = {"item_id": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


@app.get("/items_validation/{item_id}")
async def read_items_validation(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
    q: str | None = Query(None, alias="item-query"),
    size: float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
    q: str | None = None,
    item: Item = Body(..., embed=True),  # {item={}}
    # item: Item = Body(...)
):
    result = {"item_id": item_id}
    if q:
        result.update({q: q})
    if item:
        result.update({"item": item})
    return result
