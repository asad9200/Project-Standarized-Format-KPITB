"""App1 settings loaded from environment variables."""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP1_NAME", "App1")


settings = Settings()
