from pydantic import BaseModel, Field


class ProductDescSchema(BaseModel):
    product_id: int
    name: str = Field(max_length=255)
    description: str | None = Field(max_length=2048)
    barcode: str = Field(max_length=12)
    category_id: int
    is_deleted: bool