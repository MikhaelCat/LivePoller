from datetime import datetime, timedelta
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer

import jwt


SECRET_KEY = "your-super-secret-key"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token( dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
