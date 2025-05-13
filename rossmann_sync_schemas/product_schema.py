from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    product_id: int
    name: str = Field(max_length=255)
    description: str | None = Field(max_length=2048)
    barcode: str = Field(max_length=12)
    category_id: int
    price: float = Field(gt=0)
    discount: float = Field(ge=0, le=1)
    is_deleted: bool