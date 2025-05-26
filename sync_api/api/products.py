from datetime import datetime

from fastapi import APIRouter, Depends
from rossmann_oltp_models import Product, CityProduct, Shop

from database.db import get_db
from rossmann_sync_schemas import ProductSchema

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/sync", response_model=list[ProductSchema])
async def sync_products(
    shop_id: int,
    sync_utc_time: datetime,
    db=Depends(get_db),
):
    products = (
        db.query(Product, CityProduct)
        .join(CityProduct, CityProduct.product_id == Product.product_id)
        .join(Shop, Shop.city_id == CityProduct.city_id)
        .filter(
            Product.last_updated_utc >= sync_utc_time,
            Shop.shop_id == shop_id,
        )
        .all()
    )
    result = [
        ProductSchema(
            product_id=product.product_id,
            name=product.name,
            description=product.description,
            barcode=product.barcode,
            category_id=product.category_id,
            price=city_product.price,
            discount=city_product.discount,
            is_deleted=product.is_deleted,
        )
        for product, city_product in products
    ]

    return result
