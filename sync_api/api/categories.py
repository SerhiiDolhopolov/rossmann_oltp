from datetime import datetime

from fastapi import APIRouter, Depends
from rossmann_oltp_models import Category

from rossmann_oltp.db import get_db
from rossmann_sync_schemas import CategorySchema


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get('/sync', response_model=list[CategorySchema])
async def sync_categories(sync_utc_time: datetime,
                          db=Depends(get_db)):
    categories = db.query(Category) \
                   .filter(Category.last_updated_utc >= sync_utc_time) \
                   .all()
    return categories
