from pydantic import BaseModel, Field


class EmployeeSchema(BaseModel):
    employee_id: int
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    role: str = Field(max_length=50)