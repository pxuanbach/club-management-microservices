from typing import Any
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from crud import CRUDUser
from auth import verify_password, get_password_hash
from deps.db import get_async_session
from model import Users


app = FastAPI()
crud_user = CRUDUser()


@app.post(
    "/login",
    status_code=status.HTTP_200_OK,
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user_in_db: Users = crud_user.get_user_by_username(session, form_data.username)

    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found with this username.',
        )

    verified = verify_password(form_data.password, user_in_db.hashed_password)
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is wrong.',
        )

    return user_in_db