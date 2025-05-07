from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Index

from rossmann_oltp.models import SyncBase


class CityProduct(SyncBase):
    __tablename__ = "city_products"
    
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey("cities.city_id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.product_id"), primary_key=True)
    price: Mapped[float] 
    discount: Mapped[float] = mapped_column(default=0.0)
    
    city = relationship("City", back_populates="products")
    product = relationship("Product", back_populates="cities")