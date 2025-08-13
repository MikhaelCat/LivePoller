from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str
    ELASTICSEARCH_URL: str = "http://elasticsearch:9200"

    class Config:
        env_file = ".env"

try:
    settings = Settings()
except Exception as e:
    print("⚠️  Не удалось загрузить настройки из .env:", e)
    raise
