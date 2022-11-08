from datetime import timedelta
from typing import Any, List, Optional
import uuid
from fastapi import APIRouter, Form, status, Depends, HTTPException, Body, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import ORJSONResponse

from config import settings
from utils import upload_file
from deps.db import get_async_session
from crud import CRUD
from schemas import Club as ClubSchema, ClubCreate, ClubUpdate


router = APIRouter(prefix=settings.API_PATH + "/clubs")
crud = CRUD()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=List[ClubSchema]
)
async def get_clubs(
    # request_params: RequestParams = Depends(parse_common_params(Users)),
    session: AsyncSession = Depends(get_async_session),
    # user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Get all clubs
    """
    clubs = await crud.get_multi(session)
    return clubs


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ClubSchema
)
async def create_club(
    club_in: ClubCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    club = await crud.create(session, club_in)
    return club


@router.get(
    "/{club_id}",
    status_code=status.HTTP_200_OK,
    response_model=ClubSchema
)
async def get_club_by_id(
    club_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    club = await crud.get(session, club_id)
    if not club:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy câu lạc bộ này."
        )
    return club


@router.patch(
    "/{club_id}",
    status_code=status.HTTP_200_OK,
    response_model=ClubSchema
)
async def get_club_by_id(
    club_id: uuid.UUID,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    leader: Optional[uuid.UUID] = Form(None),
    is_blocked: Optional[bool] = Form(None),
    file: Optional[UploadFile] = File(None),
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    club = await crud.get(session, club_id)
    if not club:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy câu lạc bộ này."
        )
    club_in = ClubUpdate(
        name=name,
        description=description,
        leader=leader,
        is_blocked=is_blocked,
    )
    if file:
        club_in.img_url = await upload_file(file)
    club = await crud.update(session, db_obj=club, obj_in=club_in)
    return club