from pydantic_settings import BaseSettings
from datetime import date
import os


class FacultySettings(BaseSettings):
    application: str = "Faculty Management System"
    webmaster: str = "admin@erp-domain.com"
    created: date = "2025-10-01"


class LibrarySettings(BaseSettings):
    application: str = "Library Management System"
    webmaster: str = "admin@erp-domain.com"
    created: date = "2025-10-01"


class StudentSettings(BaseSettings):
    application: str = "Student Management System"
    webmaster: str = "admin@erp-domain.com"
    created: date = "2025-10-01"


class ServerSettings(BaseSettings):
    production_server: str
    prod_port: int
    development_server: str
    dev_port: int

    model_config = {"env_file": os.getcwd() + "/configuration/erp_settings.properties"}
