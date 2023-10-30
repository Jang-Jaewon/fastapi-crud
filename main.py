from fastapi import FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

description = """
App API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    dict(
        name="users",
        description="Operations with users. the **login** logic is also here.",
    ),
    dict(
        name="items",
        description="Manage items. so _fancy_ they have their own docs",
        externalDocs=dict(
            description="Items external docs", url="https://www.jvp.design"
        ),
    ),
]


app = FastAPI(
    title="TestApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact=dict(
        name="Jaewon",
        url="http://x-force.example.com/contact",
        email="test@example.com",
    ),
    license_info=dict(
        name="Apache 2.0", url="https://www.apache.org/licenses/LICENSE-2.0.html"
    ),
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
)


# @app.get("/users", tags=["users"])
# async def get_users():
#     return [dict(name="Harry"), dict(name="Ron")]


app.mount("/static", StaticFiles(directory="static"), name="static")

fake_secret_token = "coneofsilence"
fake_db = dict(
    foo=dict(id="foo", title="Foo", description="There goes my here"),
    bar=dict(id="bar", title="Bar", description="The bartenders"),
)


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", tags=["items"])
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items", response_model=Item, tags=["items"])
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item
