import random

from sqlalchemy.orm import Session

from rossmann_oltp_models import Category, Shop, City
from rossmann_oltp_models import Product, CityProduct, ShopProduct


def create_category(db: Session, name: str, description: str = None):
    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def create_product(
    db: Session,
    name: str,
    description: str,
    category: Category,
    image_url: str = None,
):
    barcode = "".join([str(random.randint(0, 9)) for _ in range(12)])
    product = Product(
        name=name,
        description=description,
        barcode=barcode,
        category=category,
        image_url=image_url,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def add_product_to_city(
    db: Session,
    product: Product,
    city: City,
    price: float,
    discount: float = 0,
) -> CityProduct:
    city_product = CityProduct(
        city=city,
        product=product,
        price=price,
        discount=discount,
    )
    db.add(city_product)
    db.commit()
    db.refresh(city_product)
    return city_product


def add_product_to_shop(
    db: Session,
    product: Product,
    shop: Shop,
    stock_quantity: int = 0,
) -> ShopProduct:
    shop_product = ShopProduct(
        shop=shop,
        product=product,
        stock_quantity=stock_quantity,
    )
    db.add(shop_product)
    db.commit()
    db.refresh(shop_product)
    return shop_product
