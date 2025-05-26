from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import SyncBase


class Product(SyncBase):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.category_id", ondelete="RESTRICT"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    barcode: Mapped[str] = mapped_column(
        String(12),
        unique=True,
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
    )
    image_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    category = relationship(
        "Category",
        back_populates="products",
    )
    shops = relationship(
        "ShopProduct",
        back_populates="product",
    )
    cities = relationship(
        "CityProduct",
        back_populates="product",
    )
