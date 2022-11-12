from fastapi import APIRouter, status, Request, Response, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from config import settings
from core import route


router = APIRouter(prefix="/auth")


@route(
    request_method=router.post,
    gateway_path='/login',
    status_code=status.HTTP_200_OK,
    form_keys=['form_data'],
    service_url=settings.USERS_SERVICE_URL,
    service_path="/api/v1/auth/login",
    authentication_required=False,
    response_model='schemas.token.Token'
)
async def login(
    request: Request, 
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(), 
):
    pass


@route(
    request_method=router.post,
    gateway_path='/token',
    status_code=status.HTTP_200_OK,
    form_keys=['form_data'],
    service_url=settings.USERS_SERVICE_URL,
    service_path="/api/v1/auth/token",
    authentication_required=False,
    response_model=None,
    include_in_schema=False
)
async def access_token(
    request: Request, 
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(), 
):
    pass


@route(
    request_method=router.post,
    gateway_path='/verify-token',
    status_code=status.HTTP_200_OK,
    form_keys=['token'],
    service_url=settings.USERS_SERVICE_URL,
    service_path="/api/v1/auth/verify-token",
    authentication_required=False,
    response_model='schemas.user.User'
)
async def verify_token(
    request: Request, 
    response: Response,
    token: str = Form(...), 
):
    pass
