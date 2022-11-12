from typing import Optional
import uuid
from fastapi import APIRouter, File, Form, UploadFile, status, Request, Response, Depends

from config import settings
from core import route
from deps import get_current_user_id


router = APIRouter(prefix="/clubs")


@route(
    request_method=router.get,
    gateway_path='',
    status_code=status.HTTP_200_OK,
    service_url=settings.CLUBS_SERVICE_URL,
    service_path="/api/v1/clubs",
    authentication_required=True,
    response_model='schemas.club.Club',
    response_list=True
)
async def get_clubs(
    request: Request, 
    response: Response,
    # search: Optional[str] = None
    current_user: str = Depends(get_current_user_id)
):
    pass


@route(
    request_method=router.post,
    gateway_path='',
    status_code=status.HTTP_200_OK,
    form_keys=["name", "description", "leader", "is_blocked", "file"],
    service_url=settings.CLUBS_SERVICE_URL,
    service_path="/api/v1/clubs",
    authentication_required=True,
    authorization_required=True,
    response_model='schemas.club.Club',
)
async def create_club(
    request: Request, 
    response: Response,
    name: str = Form(...),
    description: Optional[str] = Form(None),
    leader: uuid.UUID = Form(...),
    is_blocked: Optional[bool] = Form(None),
    file: Optional[UploadFile] = File(None),
    # search: Optional[str] = None
    current_user: str = Depends(get_current_user_id)
):
    pass


@route(
    request_method=router.get,
    gateway_path='/{club_id}',
    status_code=status.HTTP_200_OK,
    service_url=settings.CLUBS_SERVICE_URL,
    service_path="/api/v1/clubs/{club_id}",
    authentication_required=True,
    response_model='schemas.club.Club',
)
async def get_club_by_id(
    request: Request, 
    response: Response,
    club_id: uuid.UUID,
    current_user: str = Depends(get_current_user_id)
):
    pass


@route(
    request_method=router.patch,
    gateway_path='/{club_id}',
    status_code=status.HTTP_200_OK,
    form_keys=["name", "description", "leader", "is_blocked", "file"],
    service_url=settings.CLUBS_SERVICE_URL,
    service_path="/api/v1/clubs/{club_id}",
    authentication_required=True,
    authorization_required=True,
    response_model='schemas.club.Club',
)
async def update_club_by_id(
    request: Request, 
    response: Response,
    club_id: uuid.UUID,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    leader: Optional[uuid.UUID] = Form(None),
    is_blocked: Optional[bool] = Form(None),
    file: Optional[UploadFile] = File(None),
    current_user: str = Depends(get_current_user_id)
):
    pass