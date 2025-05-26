from pydantic import Field
from rossmann_sync_schemas import ProductDescSchema


class ProductSchema(ProductDescSchema):
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
        description="Unique identifier for the product category",
    )
    price: float = Field(
        gt=0,
        description="Product price",
    )
    discount: float = Field(
        default=0.0,
        ge=0,
        le=1,
        description="Discount on the product as a fraction (0 to 1)",
    )
    is_deleted: bool = Field(
        default=False,
        description="Soft deletion flag",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": 1001,
                "name": "Shampoo 250ml",
                "description": "Mild herbal shampoo",
                "barcode": "123456789012",
                "category_id": 3,
                "price": 5.99,
                "discount": 0.1,
                "is_deleted": False
            }
        }
