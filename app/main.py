from fastapi import FastAPI

from app.router import sections, users, courses
from app.database.db_setup import engine
from app.database.models import course, user

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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
app.include_router(sections.router)
