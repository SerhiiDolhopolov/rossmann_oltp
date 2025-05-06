from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import Base


class Shop(Base):
    __tablename__ = "shops"

    shop_id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(100))
    
    employees = relationship("ShopEmployee", back_populates="shop")
    products = relationship("ShopProduct", back_populates="shop")