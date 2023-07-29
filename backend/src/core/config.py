from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = 'postgresql+asyncpg://postgres:postgres@backend_postgres:5432/postgres'


settings = Settings()
