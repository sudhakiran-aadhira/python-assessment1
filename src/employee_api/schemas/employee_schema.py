from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    salary: float
    status: str
    joining_date: date
    address: str


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    salary: Optional[float] = None
    status: Optional[str] = None
    joining_date: Optional[date] = None
    address: Optional[str] = None


class EmployeeResponse(EmployeeCreate):
    id: str
