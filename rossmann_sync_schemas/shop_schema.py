from pydantic import BaseModel, Field


class ShopSchema(BaseModel):
    shop_id: int
    country_name: str = Field(max_length=50)
    city_name: str = Field(max_length=50)
    