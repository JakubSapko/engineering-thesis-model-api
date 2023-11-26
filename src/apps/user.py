from fastapi import FastAPI
from pydantic import BaseModel

from services.user_service import User_service

user_app = FastAPI(openapi_prefix="/user")

user_service = User_service()


class LoginPayload(BaseModel):
    email: str
    password: str


@user_app.get("/")
async def login():
    return {"test": "test"}


@user_app.post("/")
async def login_user(request: LoginPayload):
    login = user_service.login_user(request.email, request.password)
    return login
