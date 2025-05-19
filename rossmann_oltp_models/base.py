from datetime import datetime, timezone

from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column

from rossmann_oltp_models.config import DATE_TIME_FORMAT

@as_declarative()
class Base:
    pass

class SyncBase(Base):
    __abstract__ = True

    last_updated_utc: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        index=True
    )
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)