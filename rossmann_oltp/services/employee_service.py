import random
import uuid
from datetime import date, timedelta

from sqlalchemy.orm import Session

from employee_role import EmployeeRole
from rossmann_oltp_models import Employee


def create_employee(db: Session, 
                    first_name: str,
                    last_name: str,
                    role: EmployeeRole,
                    salary: float,
                    ) -> Employee:
    birth_date = date.today() - timedelta(days=random.randint(20, 60) * 365)
    hire_date = date.today() - timedelta(days=random.randint(0, 365*5))
    phone = '+15454545454'
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    password = "password"
    
    
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        hire_date=hire_date,
        phone=phone,
        email=email,
        role=role.value,
        password=password,
        salary=salary
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee