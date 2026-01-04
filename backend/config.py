"""Application configuration from environment variables."""

import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    # Database
    database_url: str = "mysql+pymysql://equity_user:equity_pass@localhost:3306/equity_dev"

    # Application
    environment: str = "development"

    # JWT
    secret_key: str = "dev_secret_key_not_for_production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        """Pydantic config."""

        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
