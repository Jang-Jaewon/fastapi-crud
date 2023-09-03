from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, List, Optional
from uuid import UUID

from fastapi import Body, FastAPI, Path, Query

from schema import Image, Importance, Item, Offer, User

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_date: datetime | None = Body(None),
    end_date: datetime | None = Body(None),
    repeat_at: time | None = Body(None),
    process_after: timedelta | None = Body(None),
):
    start_process = start_date + process_after
    duration = end_date - start_process
    return {
        "item_id:": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
