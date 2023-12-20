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
    email = form_data.username
    password = form_data.password

    result  = account.login(User(email=email, password=password))
    
    response = JSONResponse(content=result.get_tokens_in_dict())
    response.set_cookie(key="refresh_token", value=result.get_refresh_token(), httponly=True)

    return response

@user_route.post("/refresh", summary="Generate a new refresh token")
async def gen_token(header: Annotated[str, Header()] = None):
    return account.validate_token(header)
