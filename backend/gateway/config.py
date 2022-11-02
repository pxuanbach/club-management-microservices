import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 360
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    USERS_SERVICE_URL: str = os.environ.get('USERS_SERVICE_URL')
    CLUBS_SERVICE_URL: str = os.environ.get('CLUBS_SERVICE_URL')
    GATEWAY_TIMEOUT: int = 59


settings = Settings()