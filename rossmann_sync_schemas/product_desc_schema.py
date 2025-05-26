from pydantic import BaseModel, Field


class ProductDescSchema(BaseModel):
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
    is_deleted: bool = Field(
        default=False,
        description="Soft deletion flag",
    )

    class Config:
        json_schema_extra = {"example": {
            "product_id": 1,
            "name": "Smartphone",
            "description": "Latest model smartphone",
            "barcode": "123456789012",
            "category_id": 1,
            "is_deleted": False
        }}
