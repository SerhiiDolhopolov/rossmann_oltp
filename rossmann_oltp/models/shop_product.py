from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Index

from rossmann_oltp.models import Base


class ShopProduct(Base):
    __tablename__ = "shop_products"
    
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.shop_id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.product_id"), primary_key=True)
    stock_quantity: Mapped[int]
    
    shop = relationship("Shop", back_populates="products")
    product = relationship("Product", back_populates="shops")