from pydantic import Field

from rossmann_sync_schemas import SyncModel


class ProductDescSchema(SyncModel):
    product_id: int = Field(
        ge=1,
        description="Unique identifier for the product",
    )
    name: str = Field(
        max_length=255,
        description="Product name",
    )
    description: str | None = Field(
        default=None,
        max_length=2048,
        description="Optional product description",
    )
    barcode: str = Field(
        max_length=12,
        description="Product barcode",
    )
    category_id: int = Field(
        ge=1,
        description="Identifier of the associated category",
    )

    class Config:
        json_schema_extra = {"example": {
            "product_id": 1,
            "name": "Smartphone",
            "description": "Latest model smartphone",
            "barcode": "123456789012",
            "category_id": 1,
            "last_updated_utc": "2023-10-01T12:00:00Z",
            "is_deleted": False
        }}
