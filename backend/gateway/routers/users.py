from typing import Optional
import uuid
from fastapi import APIRouter, status, Request, Response, Depends

from config import settings
from core import route
from deps import get_current_user_id


router = APIRouter(prefix="/users")


@route(
    request_method=router.get,
    gateway_path='',
    status_code=status.HTTP_200_OK,
    service_url=settings.USERS_SERVICE_URL,
    service_path="/api/v1/users",
    authentication_required=False,
    response_model='schemas.user.User',
    response_list=True
)
async def get_users(
    request: Request, 
    response: Response,
    search: Optional[str] = None
):
    pass


@route(
    request_method=router.get,
    gateway_path='/{user_id}',
    status_code=status.HTTP_200_OK,
    service_url=settings.USERS_SERVICE_URL,
    service_path="/api/v1/users/{user_id}",
    authentication_required=True,
    response_model='schemas.user.User',
)
async def get_user_by_id(
    request: Request, 
    response: Response,
    user_id: uuid.UUID,
    current_user: str = Depends(get_current_user_id)
):
    pass