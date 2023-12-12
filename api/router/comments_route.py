from api import APIRouter, BaseModel

class NewComment(BaseModel):
    post_id: int
    comment_id: int
    user_id: int
    comment: str

comment_route = APIRouter(prefix="/comments", tags=["comments", "articles"])

@comment_route.get("/")
async def get_comments():
    raise NotImplemented()

@comment_route.get("/{post_id}")
async def get_comments_by_post_id(id: int):
    raise NotImplemented()


@comment_route.post("/")
async def add_comment(comment: NewComment):
    raise NotImplemented()

@comment_route.put("/{comment_id}")
async def update_comment(comment_id: int, comment: NewComment):
    raise NotImplemented()

@comment_route.delete("/")
async def delete_comment(id: int):
    raise NotImplemented()
