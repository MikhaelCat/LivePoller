# backend/core/security.py
import jwt
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


# --- Конфигурация ---
SECRET_KEY = "your-super-secret-key" # Используй сгенерированный ключ в production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Экземпляры ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# --- Функции ---
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет, совпадает ли открытый пароль с хэшем."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Генерирует хэш для пароля."""
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    """
    Создаёт JWT-токен с временем жизни.
    
    Args:
        data (dict): Данные для включения в токен.

    Returns:
        str: Закодированный JWT токен.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
