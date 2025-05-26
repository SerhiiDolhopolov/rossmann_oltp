from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import Base


class Terminal(Base):
    __tablename__ = "terminals"

    terminal_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    shop_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("shops.shop_id", ondelete="RESTRICT"),
        nullable=False,
    )

    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    shop = relationship(
        "Shop",
        back_populates="terminals"
    )
