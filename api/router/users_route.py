#TODO: Tarea para josu ;)
"""
Algunas tareas para hacer en este router:
    1. refactorizar el router, moviendo cada cosa a su respectivo fichero
    2. quitar toda la duplicidad
    3. cambiar la funcion create_user para que retorne un json como el siguiente: {"msg": "User creation sucess", "token": token }
    4. implementar al menos un ruta que requiera el token para poder accederse (Un gran plus ya que requiere investigar)
"""

from fastapi import APIRouter
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from uuid import uuid4
from tokens.utils import (
        get_hashed_password,
        create_access_token,
        create_refresh_token,
        verify_password
        )

from pydantic import BaseModel
from typing import Annotated

user_route = APIRouter(prefix="/users", tags=["users"])

class UserOut(BaseModel):
    email: str
    password: str
    user_id: str

class UserAuth(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

db: dict = {}


@user_route.post("/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    user = db.get(data.email, None)
    if user is not None:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists")

    user = {
            'email': data.email,
            'password': get_hashed_password(data.password),
            'user_id': str(uuid4())
            }

    db[data.email] = user #guarda el usuario en la base de datos
    return user

@user_route.post("/login", summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get(form_data.username, None)
    if user is None: #Verifica el usuario
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
                )

    hashed_pass = user["password"]

    if not verify_password(form_data.password, hashed_pass): #Verifica la contraseña
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
                )

    return {
            "access_token": create_access_token(user["email"]),
            "refresh_token": create_refresh_token(user["email"])
            }



@user_route.get("/")
async def get_users():
    return {"msg": "Not implemented"}

