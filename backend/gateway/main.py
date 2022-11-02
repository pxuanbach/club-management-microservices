from fastapi import Depends, FastAPI, status, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

from config import settings
from core import route


app = FastAPI()


@route(
    request_method=app.post,
    path='/api/login',
    status_code=status.HTTP_200_OK,
    payload_key='form_data',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func='post_processing.access_token_generate_handler',
    response_model='schemas.token.Token'
)
async def login(
    request: Request, 
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(), 
):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=int("8000"),
    )
