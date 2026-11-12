"""App2 settings loaded from environment variables."""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP2_NAME", "App2")


settings = Settings()
