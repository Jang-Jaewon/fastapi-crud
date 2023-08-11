from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.models.user import Users

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    Users().create(session, auto_commit=True)
    current_time = datetime.utcnow()
    return Response(f"FASTAPI CRUD (UTC {current_time.strftime('%Y-%m-%d %H:%M:%')})")
