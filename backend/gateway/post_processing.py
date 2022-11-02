from datetime import timedelta
import uuid

from auth import create_access_token
from config import settings
from schemas.token import Token


def access_token_generate_handler(username: str, user_id: uuid.UUID):
    token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(username, user_id, token_expires)
    return Token(token=access_token)