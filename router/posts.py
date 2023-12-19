from fastapi import APIRouter
from tests.fake_data_generator import Generators

posts_route = APIRouter(prefix="/posts", tags=["posts"])


# Public route
@posts_route.get("/")
async def get_books():
    return Generators.generate_posts(count=100)
