from datetime import datetime, timezone

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column


@as_declarative()
class Base:
    pass

class SyncBase(Base):
    __abstract__ = True

    last_updated_utc: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc),
                                                       index=True)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)