import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from employee_api.config import settings


logger = logging.getLogger(__name__)


class MongoDBService:

    def __init__(self) -> None:
        self.client = MongoClient(
            settings.mongo_uri,
            serverSelectionTimeoutMS=3000
        )

        self.database = self.client[
            settings.db_name
        ]

        self.employees = self.database[
            "employees"
        ]

    def check_connection(self) -> bool:
        try:
            self.client.admin.command("ping")
            return True

        except PyMongoError:
            logger.exception(
                "MongoDB connection failed"
            )
            return False

    def close(self) -> None:
        self.client.close()


mongo_service = MongoDBService()