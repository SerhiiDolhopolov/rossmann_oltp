from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

from rossmann_oltp_models import Base


class ShopProduct(Base):
    __tablename__ = "shop_products"
    
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.shop_id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.product_id"), primary_key=True)
    stock_quantity: Mapped[int]
    updated_at_utc: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    
    shop = relationship("Shop", back_populates="products")
    product = relationship("Product", back_populates="shops")