from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class IPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(request.__dict__)

        response = await call_next(request)

        return response
