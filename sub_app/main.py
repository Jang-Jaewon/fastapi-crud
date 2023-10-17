from fastapi import Depends, FastAPI

from .dependencies import get_token_header, get_query_token
from .routers.users import router


app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}