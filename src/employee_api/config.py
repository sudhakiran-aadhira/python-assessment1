import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.mongo_uri = os.getenv(
            "MONGO_URI",
            "mongodb://localhost:27017"
        )

        self.db_name = os.getenv(
            "DB_NAME",
            "employee_management"
        )

        self.webhook_secret = os.getenv(
            "WEBHOOK_SECRET",
            ""
        )

        self.crm_base_url = os.getenv(
            "CRM_BASE_URL",
            ""
        )


settings = Settings()
