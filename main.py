from fastapi import FastAPI

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


@app.get("/items")
async def list_items():
    return {"message": "list items route"}


@app.get("/items/{items_id}")
async def get_item(items_id: int):
    return {"items_id": items_id}


@app.get("/users")
async def list_users():
    return {"message": "list items route"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}
