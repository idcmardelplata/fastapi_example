from fastapi import APIRouter

from pydantic import BaseModel
from typing import Annotated

class NewUser(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birth: str


user_route = APIRouter(prefix="/users", tags=["users"])

@user_route.get("/")
async def get_users():
    return {"msg": "Not implemented"}

@user_route.post("/")
async def add_user(user: NewUser):
    raise NotImplemented()

@user_route.put("/{user_id}")
async def update_user(user_id: int, user: NewUser):
    raise NotImplemented()

@user_route.delete("/")
async def delete_user(id: int):
    raise NotImplemented()
