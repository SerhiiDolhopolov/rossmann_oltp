from sqlalchemy import Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp.models import SyncBase


class ShopEmployee(SyncBase):
    __tablename__ = "shop_employees"
    
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.shop_id"), primary_key=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.employee_id"), primary_key=True)
    
    shop = relationship("Shop", back_populates="employees")
    employee = relationship("Employee", back_populates="shop")
    
    __table_args__ = (
        Index(f'ix_shop_employee_sync', 'last_updated_utc'),
    )