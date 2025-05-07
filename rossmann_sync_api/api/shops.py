from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from rossmann_oltp.models import Shop, City, Country

from rossmann_oltp.db import get_db
from rossmann_sync_api.schemas import ShopSchema


router = APIRouter(prefix="/shops", tags=["shops"])


@router.get('/authorize', response_model=ShopSchema)
async def authorize_shop(shop_id: int, 
                         password: str, 
                         db: Session = Depends(get_db)):
    result = db.query(Shop, City, Country) \
             .join(City, City.city_id == Shop.city_id) \
             .join(Country, Country.country_id == City.country_id) \
             .filter(Shop.shop_id == shop_id) \
             .first()
    if not result:
        raise HTTPException(status_code=404, detail="Shop not found")
    shop, city, country = result
    if shop.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")

    shop_schema = ShopSchema(shop_id=shop.shop_id,
                             country_name=country.country_name,
                             city_name=city.city_name)
    return shop_schema
    