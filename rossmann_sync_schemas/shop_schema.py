from pydantic import BaseModel, Field


class ShopSchema(BaseModel):
    shop_id: int = Field(
        ge=1,
        description="Unique identifier for the shop",
    )
    country_name: str = Field(
        max_length=50,
        description="Name of the country where the shop is located",
    )
    city_name: str = Field(
        max_length=50,
        description="Name of the city where the shop is located",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "shop_id": 1,
                "country_name": "Germany",
                "city_name": "Berlin"
            }
        }
