from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "TaskFlow API"
    environment: Literal["local", "test", "production"]


@lru_cache
def get_settings() -> Settings:
    return Settings() #type: ignore[call-arg]
