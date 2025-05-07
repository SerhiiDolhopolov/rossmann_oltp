from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import Base


class Terminal(Base):
    __tablename__ = "terminals"

    terminal_id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.shop_id"))
    password: Mapped[str] = mapped_column(String(100))
    
    shop = relationship("Shop", back_populates="terminals")
