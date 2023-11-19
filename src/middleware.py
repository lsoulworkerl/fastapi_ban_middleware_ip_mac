import secrets

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from repositories import (
    user_ip_repository,
    user_cookie_repository,
)


class IPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        user_ip = request.scope.get('client')[0]
        user_ip_repository.create_user_ip(ip=user_ip)
        response = await call_next(request)
        return response


class CookieMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)

        cookie = request.cookies.get("evercookie")
        if cookie is not None:
            return response

        user_cookie = secrets.token_hex(10)
        user_cookie_repository.create_user_cookie(cookie=user_cookie)
        response.set_cookie(key="evercookie", value=user_cookie, max_age=3600)
        return response
