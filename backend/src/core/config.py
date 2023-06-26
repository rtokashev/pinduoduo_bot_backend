from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = 'postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres'


settings = Settings()
