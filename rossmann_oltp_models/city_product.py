from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Float

from rossmann_oltp_models import SyncBase


class CityProduct(SyncBase):
    __tablename__ = "city_products"

    city_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("cities.city_id", ondelete="CASCADE"),
        primary_key=True,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.product_id", ondelete="CASCADE"),
        primary_key=True,
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
    discount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    city = relationship(
        "City",
        back_populates="products",
    )
    product = relationship(
        "Product",
        back_populates="cities",
    )
