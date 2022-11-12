from typing import List, Optional
import aiohttp
import functools
from importlib import import_module
from fastapi import Request, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from network import make_request
from utils.body import unzip_body_object
from utils.form import unzip_form_params


def route(
        request_method, 
        gateway_path: str, 
        status_code: int,
        service_url: str,
        body_keys: Optional[List[str]] = None, 
        form_keys: Optional[List[str]] = None, 
        service_path: Optional[str] = None,
        authentication_required: bool = False,
        authentication_token_decoder: str = 'auth.verify_access_token',
        authorization_required: bool = False,
        service_authorization_checker: str = 'auth.is_admin_user',
        service_header_generator: str = 'auth.generate_request_header',
        response_model: str = None,
        response_list: bool = False,
        include_in_schema: bool = True
):
    """
    it is an advanced wrapper for FastAPI router, purpose is to make FastAPI
    acts as a gateway API in front of anything\n
    Args:
        request_method: is a callable like (app.get, app.post and so on.)
        gateway_path: is the path to bind gateway.
        service_url: is url path to microservice (like "https://api.example.com/v1")
        service_path: is the path to the endpoint on another service.
        status_code: expected HTTP(status.HTTP_200_OK) status code
        body_keys: used to extract body model from endpoint
        form_keys: used to extract form model parameters from endpoint
        authentication_required: is bool to give to user an auth priviliges
        authorization_required: is bool to give to user an authorize
        authentication_token_decoder: decodes JWT token as a proper payload
        service_authorization_checker: does simple front authorization checks
        service_header_generator: generates headers for inner services from jwt token payload # noqa
        response_model: shows return type and details on api docs
        response_list: decides whether response structure is list or not
        include_in_schema: include openapi docs
    Returns:
        wrapped endpoint result as is
    """

    # request_method: app.post || app.get or so on
    # app_any: app.post('/api/login', status_code=200, response_model=int)
    if response_model:
        response_model = import_function(response_model)
        if response_list:
            response_model = List[response_model]

    app_any = request_method(
        gateway_path, 
        status_code=status_code,
        response_model=response_model,
        include_in_schema=include_in_schema
    )

    def wrapper(f):
        @app_any
        @functools.wraps(f)
        async def inner(request: Request, response: Response, **kwargs):
            service_headers = {}

            if authentication_required:
                # authentication
                authorization = request.headers.get('authorization')
                token = authorization.replace("Bearer ", "")
                token_decoder = import_function(authentication_token_decoder)
                exc = None
                try:
                    token_payload = token_decoder(token)
                except Exception as e:
                    # in case a new decoder is used by dependency injection and
                    # there might be an unexpected error
                    exc = str(e)
                finally:
                    if exc:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=exc,
                            headers={'WWW-Authenticate': 'Bearer'},
                        )

                # authorization
                if authorization_required:
                    authorization_checker = import_function(
                        service_authorization_checker
                    )
                    is_user_eligible = authorization_checker(token_payload)
                    if not is_user_eligible:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail='Tài khoản không đủ quyền.',
                            headers={'WWW-Authenticate': 'Bearer'},
                        )

                # service headers
                if service_header_generator:
                    header_generator = import_function(
                        service_header_generator
                    )
                    service_headers = header_generator(token_payload)

            scope = request.scope

            method = scope['method'].lower()
            gateway_path = scope['path']
            query_string = scope['query_string'].decode('UTF-8')
            path_params = scope["path_params"]  # dict like { 'user_id': 'xxxxx' }
            content_type = str(request.headers.get('Content-Type'))

            # OAuth2PasswordRequestForm
            request_form = (
                await request.form() if 'x-www-form-urlencoded' in content_type else None
            )
            print(kwargs)
            request_body = await unzip_body_object(
                necessary_params=body_keys,
                all_params=kwargs,
            )
            request_form = await unzip_form_params(
                necessary_params=form_keys,
                request_form=request_form,
                all_params=kwargs,
            )

            payload = request_body
            if request_form:
                payload = request_form
            
            prepare_microservice_path = f"{service_url}{gateway_path}"
            if service_path:
                prepare_microservice_path = f"{service_url}{service_path}"

            # handle path params
            microservice_url = prepare_microservice_path.format(**path_params)

            # handle query params
            if query_string:
                microservice_url = microservice_url + "?" + query_string

            try:
                resp_data, status_code_from_service = await make_request(
                    url=microservice_url,
                    method=method,
                    data=payload,
                    headers=service_headers,
                )
            except aiohttp.client_exceptions.ClientConnectorError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail='Service is unavailable.',
                    headers={'WWW-Authenticate': 'Bearer'},
                )
            except aiohttp.client_exceptions.ContentTypeError:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Service error.',
                    headers={'WWW-Authenticate': 'Bearer'},
                )

            response.status_code = status_code_from_service
            if status_code_from_service >= 400 and status_code_from_service < 500:
                raise HTTPException(
                    status_code=status_code_from_service,
                    detail=resp_data.get("detail")
                )

            return resp_data

    return wrapper


def import_function(method_path):
    module, method = method_path.rsplit('.', 1)
    mod = import_module(module)
    return getattr(mod, method, lambda *args, **kwargs: None)