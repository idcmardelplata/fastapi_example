from fastapi import APIRouter
# from fastapi import status, HTTPException, Depends
# from fastapi.security import OAuth2PasswordRequestForm
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
# class UserAuth(BaseModel):
#     email: str
#     password: str
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

@user_route.get("/")
async def get_users():
    return {"msg": "Not implemented"}

