from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class Auth(BaseHTTPMiddleware):
    def __init__(self):
        pass

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response