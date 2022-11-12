from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 360
    SECRET_KEY: str 
    USERS_SERVICE_URL: str
    CLUBS_SERVICE_URL: str
    GATEWAY_TIMEOUT: int = 59


settings = Settings()