from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import item_router, user_router

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(user_router)
app.include_router(item_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
