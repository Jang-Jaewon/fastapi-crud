from fastapi import FastAPI
from api import users, courses

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

app.include_router(users.router)
app.include_router(courses.router)
