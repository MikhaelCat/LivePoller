from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str
    ELASTICSEARCH_URL: str = "http://elasticsearch:9200"

    class Config:
        env_file = ".env"


settings = Settings()
