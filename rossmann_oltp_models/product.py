from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import SyncBase


class Product(SyncBase):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    barcode: Mapped[str] = mapped_column(String(12), unique=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.category_id"))
    image_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    
    category = relationship("Category", back_populates="products")
    shops = relationship("ShopProduct", back_populates="product")
    cities = relationship("CityProduct", back_populates="product")