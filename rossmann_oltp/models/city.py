from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import Base


class City(Base):
    __tablename__ = "cities"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.country_id"))
    city_name: Mapped[str] = mapped_column(String(50))
    
    country = relationship("Country", back_populates="cities")
    products = relationship("CityProduct", back_populates="city")
    shops = relationship("Shop", back_populates="city")