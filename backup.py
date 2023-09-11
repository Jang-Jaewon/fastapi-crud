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
    size: float = Query(..., gt=0, lt=7.75),
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


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., embed=True),  # {item={}}
):
    result = {"item_id": item_id, "item": item}
    return result


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
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


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_date: datetime | None = Body(None),
    end_date: datetime | None = Body(None),
    repeat_at: time | None = Body(None),
    process_after: timedelta | None = Body(None),
):
    start_process = start_date + process_after
    duration = end_date - start_process
    return {
        "item_id:": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


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


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item


@app.post("/items{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["Foo", "Bar", "Baz"]):
    return items[item_id]


@app.get(
    "/items{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: Literal["Foo", "Bar", "Baz"]):
    return items[item_id]


@app.post(
    "/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"}
)
async def read_items_public_data(item_id: Literal["Foo", "Bar", "Baz"]):
    return items[item_id]


items = {
    "item1": {"description": "this is description hello", "type": "car"},
    "item2": {
        "description": "Music is my dog, it my icecream",
        "type": "plane",
        "size": 5,
    },
}


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User 'saved'.")
    return user_in_db


@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]


list_items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/list_items/", response_model=list[ListItem])
async def read_items():
    return items


@app.get("/arbitrary", response_model=dict[str, float])
async def get_arbitrary():
    return {"foo": 1, "bar": 2}


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


@app.post("/file")
async def create_file(
    files: list[bytes] = File(..., description="A file read as bytes")
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile")
async def create_upload_file(
    files: list[UploadFile] = File(..., description="A file read as UploadFile")
):
    return {"filename": [file.filename for file in files]}
