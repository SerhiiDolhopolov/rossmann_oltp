from datetime import datetime, timezone

from sqlalchemy.orm import Session

from rossmann_oltp_models import ShopProduct
from database.config import DATE_TIME_FORMAT


def update_products_quantity(
    db: Session,
    shop_id: int,
    products_quantity: dict[int, int],
):
    """
    Args:
        db (Session): db
        shop_id (int): shop id
        products_quantity (dict[int, int]): {product_id: quantity}
    """
    for product_id, quantity in products_quantity.items():
        db.query(ShopProduct).filter(
            ShopProduct.shop_id == shop_id,
            ShopProduct.product_id == product_id,
        ).update(
            {
                "stock_quantity": quantity,
                "updated_at_utc": datetime.now(timezone.utc).strftime(DATE_TIME_FORMAT),
            }
        )
    db.commit()
