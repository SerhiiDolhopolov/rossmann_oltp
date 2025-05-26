from datetime import date

from sqlalchemy import Integer, Float, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import SyncBase


class Employee(SyncBase):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    shop_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("shops.shop_id", ondelete="SET NULL"),
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    hire_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    phone: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        nullable=False,
    )
    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    salary: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    shop = relationship(
        "Shop",
        back_populates="employees",
    )
