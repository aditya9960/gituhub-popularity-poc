from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str
    API_V1_PREFIX: str
    API_V2_PREFIX: str
    REDIS_URL: str
    CACHE_TTL_SECONDS: int
    SECRET_KEY: str
    GITHUB_TOKEN: Optional[str] = None
    # set for .env
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

settings = Settings()