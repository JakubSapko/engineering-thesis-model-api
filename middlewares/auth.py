from fastapi import Request
from fastapi.responses import JSONResponse
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

        login, password = data.get("login"), data.get("password")
        print(login, password)
        if not (login and password):
            return JSONResponse(status_code=400, content="Incorrect payload")
        if login != "test" or password != "test":
            return JSONResponse(status_code=400, content="Incorrect login or password")

        response = await call_next(request)

        return response
