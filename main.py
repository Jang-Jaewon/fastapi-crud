from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Header, Path, Query, status, Form, File, UploadFile

from schema import (Image, Importance, Item, Offer, User, UserBase, UserIn, PlaneItem, CarItem,
                    UserInDB, UserOut, ListItem)

app = FastAPI()


@app.post("file")
async def create_file(file: bytes | None = File(None, description="A file read as bytes")):
    return {"file": len(file)}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(..., description="A file read as UploadFile")):
    if not file:
        return {"message": "No upload file send"}
    return {"filename": file.filename}
