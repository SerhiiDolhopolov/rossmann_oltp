from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
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
    is_deleted: bool = Field(
        default=False,
        description="Soft deletion flag",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "category_id": 1,
                "name": "Electronics",
                "description": "Devices and gadgets",
                "is_deleted": False,
            }
        }
