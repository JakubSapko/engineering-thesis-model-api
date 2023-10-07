from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next):
        await self.set_body(request)
        data = await request.json()
        print(data)
        response = await call_next(request)

        return response
