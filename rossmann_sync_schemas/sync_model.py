from datetime import datetime
from pydantic import BaseModel, Field


class SyncModel(BaseModel):
    is_deleted: bool = Field(
        default=False,
        description="Soft deletion flag",
    )
    updated_at_utc: datetime = Field(
        description="Last updated timestamp in UTC",
    )
    