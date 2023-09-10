from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query, status, Form, File, UploadFile

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


@app.post("/file")
async def create_file(files: list[bytes] = File(..., description="A file read as bytes")):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile")
async def create_upload_file(files: list[UploadFile] = File(..., description="A file read as UploadFile")):
    return {"filename":[file.filename for file in files]}
