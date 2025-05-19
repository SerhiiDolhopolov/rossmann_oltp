from datetime import datetime, timezone

from sqlalchemy import event
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column

from rossmann_oltp_models.config import DATE_TIME_FORMAT

@as_declarative()
class Base:
    pass

class SyncBase(Base):
    __abstract__ = True

    last_updated_utc: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc).strftime(DATE_TIME_FORMAT),
                                                       index=True)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    
def update_last_updated_utc(mapper, connection, target):
    from datetime import datetime, timezone
    from rossmann_oltp_models.config import DATE_TIME_FORMAT
    target.last_updated_utc = datetime.now(timezone.utc).strftime(DATE_TIME_FORMAT)

for cls in SyncBase.__subclasses__():
    event.listen(cls, "before_update", update_last_updated_utc)