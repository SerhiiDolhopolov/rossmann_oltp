from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from rossmann_oltp_models import Employee

from rossmann_oltp.db import get_db
from rossmann_sync_schemas import EmployeeSchema


router = APIRouter(prefix="/employees", tags=["employees"])


@router.get('/authorize', response_model=EmployeeSchema)
async def authorize_employee(email: EmailStr, 
                             password: str, 
                             db: Session = Depends(get_db)):
    employee = db.query(Employee) \
                 .filter(Employee.email == email) \
                 .first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    if employee.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")
    employee_schema = EmployeeSchema(employee_id=employee.employee_id,
                                     first_name=employee.first_name,
                                     last_name=employee.last_name,
                                     role=employee.role)
    return employee_schema
