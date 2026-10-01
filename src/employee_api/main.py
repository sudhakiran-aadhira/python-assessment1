from fastapi import FastAPI

from employee_api.api.routes import router
from employee_api.utils.logger import configure_logging


configure_logging()


app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


app.include_router(router)