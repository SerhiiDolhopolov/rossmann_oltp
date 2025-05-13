from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    category_id: int
    name: str = Field(max_length=255)
    description: str | None = Field(max_length=2048, default=None)
    is_deleted: bool
    