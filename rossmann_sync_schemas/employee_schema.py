from pydantic import BaseModel, Field
from rossmann_sync_schemas.employee_role import EmployeeRole


class EmployeeSchema(BaseModel):
    employee_id: int = Field(
        ge=1,
        description="Unique identifier for the employee",
    )
    first_name: str = Field(
        max_length=50,
        description="Employee's first name",
    )
    last_name: str = Field(
        max_length=50,
        description="Employee's last name",
    )
    role: EmployeeRole = Field(
        description="Employee's role",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "employee_id": 1,
                "first_name": "Steve",
                "last_name": "Jobs",
                "role": EmployeeRole.CASHIER,
            }
        }
