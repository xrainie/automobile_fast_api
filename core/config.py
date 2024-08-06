from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os


load_dotenv()

PRODUCTION = False


class Settings(BaseSettings):
    db_url: str = os.environ.get("DB_URL")
    echo: bool = True if not PRODUCTION else False


settings = Settings()