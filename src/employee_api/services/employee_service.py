import logging
from typing import Any

from bson import ObjectId

from employee_api.database import mongo_service
from employee_api.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate
)


logger = logging.getLogger(__name__)


class EmployeeService:

    def create(
        self,
        employee: EmployeeCreate
    ) -> dict[str, Any]:

        data = employee.model_dump()

        result = mongo_service.employees.insert_one(
            data
        )

        data["id"] = str(
            result.inserted_id
        )

        logger.info(
            "Employee created: %s",
            data["id"]
        )

        return data

    def list(
        self,
        page: int = 1,
        limit: int = 10
    ) -> list[dict[str, Any]]:

        skip = (page - 1) * limit

        cursor = (
            mongo_service.employees
            .find()
            .skip(skip)
            .limit(limit)
        )

        employees = []

        for document in cursor:
            document["id"] = str(
                document.pop("_id")
            )

            employees.append(document)

        return employees

    def get(
        self,
        employee_id: str
    ) -> dict[str, Any] | None:

        if not ObjectId.is_valid(employee_id):
            return None

        document = mongo_service.employees.find_one(
            {"_id": ObjectId(employee_id)}
        )

        if document is None:
            return None

        document["id"] = str(
            document.pop("_id")
        )

        return document

    def update(
        self,
        employee_id: str,
        employee: EmployeeUpdate
    ) -> dict[str, Any] | None:

        if not ObjectId.is_valid(employee_id):
            return None

        update_data = employee.model_dump(
            exclude_none=True
        )

        mongo_service.employees.update_one(
            {"_id": ObjectId(employee_id)},
            {"$set": update_data}
        )

        return self.get(employee_id)

    def delete(
        self,
        employee_id: str
    ) -> bool:

        if not ObjectId.is_valid(employee_id):
            return False

        result = mongo_service.employees.delete_one(
            {"_id": ObjectId(employee_id)}
        )

        return result.deleted_count == 1


employee_service = EmployeeService()
def replace(
    self,
    employee_id: str,
    employee: EmployeeCreate
) -> dict[str, Any] | None:

    if not ObjectId.is_valid(employee_id):
        return None

    result = mongo_service.employees.replace_one(
        {"_id": ObjectId(employee_id)},
        employee.model_dump()
    )

    if result.matched_count == 0:
        return None

    return self.get(employee_id)


