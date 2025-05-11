from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import SyncBase


class Category(SyncBase):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(2048), nullable=True)
        
    products = relationship("Product", back_populates="category")