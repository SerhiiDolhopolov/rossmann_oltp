from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import Base


class Country(Base):
    __tablename__ = "countries"

    country_id: Mapped[int] = mapped_column(primary_key=True)
    country_name: Mapped[str] = mapped_column(String(50))
    
    cities = relationship("City", back_populates="country")
            