from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from api.account import Account, User
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

user_route = APIRouter(prefix="/users", tags=["users"])

account = Account()

@user_route.post("/signin", summary="Create new user")
async def signin(user: User):
    if account.register(user):
        return {"msg": "user added sucefully"}
    return {"msg": f"error on register {user.email}"}

@user_route.post("/login", summary="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    #TODO: debo retornar el refresh_token en una cookie seteada con only http
    username = form_data.username
    password = form_data.password

    result = account.login(User(email=username, password=password))
    token = result["msg"]["Loggin sucess"]["refresh_token"]
    response = JSONResponse(content=result)
    response.set_cookie(key="refresh_token", value=token, httponly=True)

    return response

@user_route.post("/refresh", summary="Generate a new refresh token")
async def gen_token(header: Annotated[str, Header()] = None):

    user_id = account.read_refresh_token(header)["user_id"]
    if account.exists_refresh_token(header):
        new_auth_token = account.create_auth_token(user_id)
        return {"Authorization: Bearer ": new_auth_token}

    return {"error": "Invalid token"}
