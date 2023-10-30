from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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
    dict(name="users", description="Operations with users. the **login** logic is also here."),
    dict(
        name="items",
        description="Manage items. so _fancy_ they have their own docs",
        externalDocs=dict(
            description="Items external docs",
            url="https://www.jvp.design"
        ),
    )
]


app = FastAPI(
    title="TestApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact=dict(
        name="Jaewon",
        url="http://x-force.example.com/contact",
        email="test@example.com"
    ),
    license_info=dict(
        name="Apache 2.0",
        url="https://www.apache.org/licenses/LICENSE-2.0.html"
    ),
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json"
)


@app.get("/users", tags=["users"])
async def get_users():
    return [dict(name="Harry"), dict(name="Ron")]

@app.get("/items/", tags=["items"])
async def read_items():
    return [dict(name="wand"), dict(name="flying broom")]


app.mount("/static", StaticFiles(directory="static"), name="static")
