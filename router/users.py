from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from api.account import Account, User
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

# from fastapi.responses import RedirectResponse
# from fastapi.responses import JSONResponse
# from servicios.usercrudservice import CreateUser, UpdateUser, DeleteUser
# from servicios.userauth import Login, Logout
# from uuid import uuid4
# from tokens.utils import (
#         get_hashed_password,
#         create_access_token,
#         create_refresh_token,
#         verify_password
#         )
#
# from pydantic import BaseModel
# from typing import Annotated
#
user_route = APIRouter(prefix="/users", tags=["users"])

# class NewUser(BaseModel):
#     email: str
#     password: str
#     user_id: str
#
#
# class TokenSchema(BaseModel):
#     access_token: str
#     refresh_token: str
#
# db: dict = {}
#

# @user_route.post("/signup", summary="Create new user", response_model=NewUser)
# async def create_user(data: UserAuth):
#     serv = CreateUser(data, db)
#
#     if serv.already_exists():
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exists madafaka")
#     else:
#         return serv.create()
#
# @user_route.post("/login", summary="Create access and refresh tokens for user", response_model=TokenSchema)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     serv = Login(form_data,db)
#
#     if not serv.exists_user(): #Verifica el usuario
#         raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Incorrect email or password"
#                 )
#     
#     
#     if not serv.is_pass_right():
#         raise HTTPException(
#                 status_code = status.HTTP_400_BAD_REQUEST,
#                 detail="Incorrect email or password"
#                 )
#
#     tokens = serv.get_tokens()
#     return JSONResponse(content="{'message':'User loged. Can get into in!'}]", headers=tokens)
#
#

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
        return {"X-Auth-token": new_auth_token}

    return {"error": "Invalid token"}
