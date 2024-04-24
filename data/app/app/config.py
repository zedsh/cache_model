import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    HTTP_PORT: int = 8000

    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: int = os.environ.get('DB_PORT')
    DB_USER: str = os.environ.get('DB_USER')
    DB_PASS: str = os.environ.get('DB_PASS')
    DB_NAME: str = os.environ.get('DB_NAME')
    @property
    def DATABASE_URL(self) -> str:  # noqa: N802
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

settings = Settings()
