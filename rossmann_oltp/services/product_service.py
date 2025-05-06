import random

from sqlalchemy.orm import Session

from models import Category, Product, Shop, ShopProduct


def create_category(db: Session, name: str, description: str = None):
    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_product(db: Session, 
                   name: str, 
                   description: str, 
                   category: Category,
                   image_url: str = None):
    barcode = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    product = Product(name=name, 
                      description=description, 
                      barcode=barcode,
                      category=category,
                      image_url=image_url)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def add_product_to_shop(db: Session,
                        product: Product,
                        shop: Shop,
                        stock_quantity: int,
                        price: float,
                        discount: float = 0):
    shop_product = ShopProduct(
        shop=shop,
        product=product,
        price=price,
        stock_quantity=stock_quantity,
        discount=discount
    )
    db.add(shop_product)    
    db.commit()
    db.refresh(shop_product)
    return shop_product