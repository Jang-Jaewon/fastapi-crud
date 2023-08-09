from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.courses import create_course, get_course, get_courses
from db.db_setup import get_db
from schemas.course import Course, CourseCreate

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses
