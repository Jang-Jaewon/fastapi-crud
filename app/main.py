import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    c = conf()
    app = FastAPI(
        title="Fast API CRUD",
        description="FastAPI CRUD Study",
        version="0.0.1",
        contact={
            "name": "Jaewon",
            "email": "jewon119@google.com",
        },
        license_info={
            "name": "MIT",
        },
    )

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
