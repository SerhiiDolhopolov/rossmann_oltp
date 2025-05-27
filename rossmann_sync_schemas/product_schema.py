from pydantic import Field
from rossmann_sync_schemas import ProductDescSchema


class ProductSchema(ProductDescSchema):
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
                "updated_at_utc": "2023-10-01T12:00:00Z",
                "is_deleted": False
            }
        }
