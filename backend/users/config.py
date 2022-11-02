import os
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 360
    DATABASE_URL: PostgresDsn
    ASYNC_DATABASE_URL: Optional[PostgresDsn]

    @validator("DATABASE_URL", pre=True)
    def build_test_database_url(cls, v: Optional[str], values: Dict[str, Any]):
        """Replace postgres with postgresql"""
        if v.startswith("postgres://"):
            v = v.replace("postgres://", "postgresql://", 1)
        return v

    @validator("ASYNC_DATABASE_URL")
    def build_async_database_url(cls, v: Optional[str], values: Dict[str, Any]):
        """Builds ASYNC_DATABASE_URL from DATABASE_URL."""
        v = values["DATABASE_URL"]
        return v.replace("postgresql", "postgresql+asyncpg") if v else v


settings = Settings()