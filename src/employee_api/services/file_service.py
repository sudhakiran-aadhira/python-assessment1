import csv
import logging
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from employee_api.schemas.employee_schema import (
    EmployeeCreate
)


logger = logging.getLogger(__name__)


class FileProcessor:

    def process_csv(
        self,
        file_path: Path
    ) -> dict[str, Any]:

        successful = []
        failed = []

        try:

            with file_path.open(
                "r",
                encoding="utf-8",
                newline=""
            ) as file:

                reader = csv.DictReader(file)

                required_columns = {
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "department",
                    "designation",
                    "salary",
                    "status",
                    "joining_date",
                    "address"
                }

                if not reader.fieldnames:
                    raise ValueError(
                        "CSV has no headers"
                    )

                missing = (
                    required_columns
                    - set(reader.fieldnames)
                )

                if missing:
                    raise ValueError(
                        f"Missing columns: {missing}"
                    )

                for line_number, row in enumerate(
                    reader,
                    start=2
                ):

                    if not any(row.values()):
                        continue

                    try:

                        employee = EmployeeCreate(
                            **row
                        )

                        successful.append(
                            employee.model_dump()
                        )

                    except (
                        ValidationError,
                        ValueError,
                        KeyError
                    ) as error:

                        failed.append(line_number)

                        logger.warning(
                            "Invalid CSV row %s: %s",
                            line_number,
                            error
                        )

        except FileNotFoundError:
            logger.exception(
                "CSV file not found: %s",
                file_path
            )
            raise

        return {
            "successful": successful,
            "failed_rows": failed,
            "total_success": len(successful),
            "total_failed": len(failed)
        }


file_processor = FileProcessor()