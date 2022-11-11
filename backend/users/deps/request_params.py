import json
from typing import List, Optional
from urllib.parse import unquote
from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.ext.declarative import DeclarativeMeta

from config import settings
from schemas import RequestParams


def parse_common_params(model: DeclarativeMeta) -> RequestParams:
    def inner(
        search: Optional[str] = None
    ):
        if search:
            search = unquote(search)
            search = search.lower()
        return RequestParams(search=search)

    return inner