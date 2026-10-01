import requests
from fastapi import APIRouter, HTTPException, Query
from fastapi import status

from employee_api.database import mongo_service
from employee_api.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate
)
from employee_api.services.employee_service import (
    employee_service
)


router = APIRouter()


@router.get("/employees")
def list_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return employee_service.list(
        page,
        limit
    )


@router.get("/employees/{employee_id}")
def get_employee(
    employee_id: str
):

    employee = employee_service.get(
        employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.post(
    "/employees",
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee: EmployeeCreate
):

    if not mongo_service.check_connection():
        raise HTTPException(
            status_code=503,
            detail="MongoDB unavailable"
        )

    return employee_service.create(
        employee
    )
@router.put("/employees/{employee_id}")
def replace_employee(
    employee_id: str,
    employee: EmployeeCreate
):

    updated = employee_service.replace(
        employee_id,
        employee
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated


@router.patch("/employees/{employee_id}")
def update_employee(
    employee_id: str,
    employee: EmployeeUpdate
):

    updated = employee_service.update(
        employee_id,
        employee
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated


@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: str
):

    deleted = employee_service.delete(
        employee_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }


@router.get("/health")
def health():

    if not mongo_service.check_connection():
        raise HTTPException(
            status_code=503,
            detail="MongoDB unavailable"
        )

    return {
        "status": "healthy"
    }
from employee_api.config import settings
from employee_api.services.external_api_service import (
    ExternalAPIClient
)
