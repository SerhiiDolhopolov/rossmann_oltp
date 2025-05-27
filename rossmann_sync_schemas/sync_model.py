from datetime import datetime
from pydantic import BaseModel, Field


class SyncModel(BaseModel):
    is_deleted: bool = Field(
        default=False,
        description="Soft deletion flag",
    )
    last_updated_utc: datetime = Field(
        description="Last updated timestamp in UTC",
    )
    