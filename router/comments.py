from datetime import datetime
from fastapi import APIRouter, Depends, Header
from typing import Annotated
from tests.fake_data_generator import Generators
from jwt.exceptions import ExpiredSignatureError 

comments_route = APIRouter(prefix="/comments", tags=["comments"])

#NOTE:
"""
Dado que el repositorio es unicamente una instancia en ram
entonces (para no persistir nada) simplemente uso la misma instancia
que use en user_route para no perder los datos.
"""
from .users import account


@comments_route.get("/", summary="Protected route")
async def get_comments(auth_bearer: Annotated[str, Header]):
    try:
        token = account.read_auth_token(auth_bearer)
        user_id = token["user_id"]

        if user_id in account.get_all_users_by_id():
            return Generators.gen_comments(count=100)

    except ExpiredSignatureError:
        return {"msg": "Token was expired, please refresh session using refresh-token"}
