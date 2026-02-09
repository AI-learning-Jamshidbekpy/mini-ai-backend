
import os
from functools import cache
# from pathlib import Path
# from typing import Literal


from pydantic_settings import BaseSettings, SettingsConfigDict, PydanticBaseSettingsSource


ENV_FILE_PATH = (
    {
        "local": ".env",
    }
).get(os.getenv("ENV", "local"), ".env")

class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        extra="allow",
    )


    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return super().settings_customise_sources(
            settings_cls,
            init_settings,
            dotenv_settings,
            env_settings,
            file_secret_settings,
        )
    API_V1: str = "api/v1/"
    app_title: str = "mini-ai-backend"
    root_path: str = ""

    MAX_FILE_MB: int = 5
    REQUIRED_COLUMNS: str = "age,height,weight"
    STRICT_VALIDATION: bool = True

    @property
    def required_columns_list(self) -> list[str]:
        return [c.strip() for c in self.REQUIRED_COLUMNS.split(",") if c.strip()]


    debug: bool = True

@cache
def get_settings() -> Settings:
    return Settings()
    



