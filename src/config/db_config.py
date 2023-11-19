from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE_HOST: str
    POSTGRES_DATABASE_PORT: str
    POSTGRES_DATABASE: str
    DB_ECHO_LOG: bool

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_DATABASE_HOST}:{self.POSTGRES_DATABASE_PORT}"
            f"/{self.POSTGRES_DATABASE}"
        )

    class Config:
        env_file = "../.env"
        extra = "ignore"


settings_db = ConfigDataBase()
