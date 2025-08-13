# backend/database/session.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Используем именованные аргументы
AsyncSessionLocal = sessionmaker(
    bind=engine,          # ← bind как именованный аргумент
    class_=AsyncSession,  # ← class_ как именованный аргумент
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
