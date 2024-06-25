import os
from dataclasses import dataclass
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask

load_dotenv()


def is_true(val: str = "") -> bool:
    if not val:
        return False
    val_comp = val.lower()
    return val_comp[0] in ("t", "1")


@dataclass
class Config:
    DEVELOPMENT: bool = is_true(os.getenv("DEVELOPMENT"))
    DEBUG: bool = is_true(os.getenv("DEBUG"))
    TESTING: bool = is_true(os.getenv("TESTING"))
    ENV: str = os.getenv("ENV", "development").lower()
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_DBNAME: str = os.getenv("DB_DBNAME")


configuration = Config()
application = Flask(__name__)
CORS(application)
application.config.from_object(configuration)