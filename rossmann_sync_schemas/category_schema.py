from pydantic import Field

from rossmann_sync_schemas import SyncModel


class CategorySchema(SyncModel):
    category_id: int = Field(
        ge=1,
        description="Unique identifier for the category",
    )
    name: str = Field(
        max_length=255,
        description="Category name",
    )
    description: str | None = Field(
        default=None,
        max_length=2048,
        description="Optional category description",
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "category_id": 1,
                "name": "Electronics",
                "description": "Devices and gadgets",
                "updated_at_utc": "2023-10-01T12:00:00Z",
                "is_deleted": False,
            }
        }
