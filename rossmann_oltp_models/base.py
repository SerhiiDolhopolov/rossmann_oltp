from datetime import datetime, timezone

from sqlalchemy import event
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column

@as_declarative()
class Base:
    pass

class SyncBase(Base):
    __abstract__ = True

    last_updated_utc: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        index=True
    )
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        event.listen(cls, "before_update", update_last_updated_utc)

def update_last_updated_utc(mapper, connection, target):
    target.last_updated_utc = datetime.now(timezone.utc)