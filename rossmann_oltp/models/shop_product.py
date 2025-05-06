from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Index

from models import SyncBase


class ShopProduct(SyncBase):
    __tablename__ = "shop_products"
    
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.shop_id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.product_id"), primary_key=True)
    price: Mapped[float] 
    discount: Mapped[float] = mapped_column(default=0.0)
    stock_quantity: Mapped[int]
    
    shop = relationship("Shop", back_populates="products")
    product = relationship("Product", back_populates="shops")

    __table_args__ = (
        Index(f'ix_shop_product_sync', 'last_updated_utc'),
    )