from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

FILES_DIR = Path("files")
FILES_DIR.mkdir(exist_ok=True)


class Settings(BaseSettings):
    """Load env once"""

    LANGSMITH_TRACING: bool = True
    LANGSMITH_API_KEY: str | None = None
    OPENAI_API_KEY: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
