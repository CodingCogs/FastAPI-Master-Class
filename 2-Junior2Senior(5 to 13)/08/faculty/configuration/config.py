from pydantic import BaseSettings
from datetime import date
import os


class FacultySettings(BaseSettings):
    application: str = "Faculty Management System"
    webmaster: str = "sjctrags@erp-domain.com"
    created: date = "2021-11-10"


class ServerSettings(BaseSettings):
    production_server: str
    prod_port: int
    development_server: str
    dev_port: int

    model_config = {"env_file": os.getcwd() + "/configuration/erp_settings.properties"}
