from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application settings
    """
    APP_NAME: str = "FastAPI Application"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # API Settings
    API_V1_PREFIX: str = "/api/v1"

    # Database Settings
    DATABASE_URL: str = "sqlite:///./app.db"

    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance
    """
    return Settings()
