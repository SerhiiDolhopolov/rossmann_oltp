from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import SyncBase


class Category(SyncBase):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(2048), nullable=True)
        
    products = relationship("Product", back_populates="category")
    
    __table_args__ = (
        Index(f'ix_category_sync', 'last_updated_utc'),
    )