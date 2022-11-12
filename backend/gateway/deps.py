from fastapi import Depends, status, Response
from fastapi.security import OAuth2PasswordBearer

from config import settings
from auth import verify_access_token

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/v1/auth/token",
)

async def get_current_user_id(
    token: str = Depends(reusable_oauth2)
) -> str:
    token_payload = verify_access_token(token)
    return token_payload