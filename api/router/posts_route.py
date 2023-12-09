from fastapi import APIRouter
from pydantic import BaseModel

class NewPost(BaseModel):
    user_id: int
    content: str


post_route = APIRouter(prefix="/posts", tags=["posts", "articles"])

@post_route.get("/")
async def get_posts():
    raise NotImplemented()


@post_route.get("/{user_id}")
async def get_posts_by_user_id(user_id: int):
    raise NotImplemented()
    

@post_route.post("/")
async def add_post(post: NewPost):
    raise NotImplemented()

@post_route.put("/{post_id}")
async def update_post(post_id: int, post: NewPost):
    raise NotImplemented()

@post_route.delete("/")
async def delete_post(id: int):
    raise NotImplemented()
