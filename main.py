import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union
from uuid import UUID

from fastapi.middleware.cors import CORSMiddleware
from fastapi import (Body, Cookie, Depends, FastAPI, File, Form, Header,
                     HTTPException, Path, Query, Request, UploadFile, status)
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (http_exception_handler,
                                        request_validation_exception_handler)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from schema import (CarItem, Image, Importance, Item, ListItem, Offer,
                    PlaneItem, Token, TokenData, User, UserBase, UserIn,
                    UserInDB, UserOut)

app = FastAPI()


