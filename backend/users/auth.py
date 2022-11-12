from datetime import timedelta, datetime
from typing import Optional
import uuid
from passlib.context import CryptContext
from jose import jwt
from pydantic import ValidationError
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from config import settings
from schemas import TokenPayload


ALGORITHM = "HS256"
SECRET_KEY = settings.SECRET_KEY


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(
    username: str, 
    user_id: uuid.UUID, 
    is_superuser: bool = False, 
    expires_delta: Optional[timedelta] = None
):
    encode = {"sub": username, "id": str(user_id), "is_superuser": is_superuser}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def verify_access_token(token: str):
    payload = None
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_payload = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Không xác thực được danh tính.",
        )
    return token_payload