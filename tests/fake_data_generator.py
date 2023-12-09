from faker import Faker
from mdgen import MarkdownPostProvider
import random
import json

fake = Faker(locale = ['es-AR'])
fake.add_provider(MarkdownPostProvider)

class Generators:
    @staticmethod
    def generate_users(count: int):
        users = []
        # metadata = {}

        for _, idx in enumerate(range(count)):
            users.append({
                "id": idx,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email":  fake.email(),
                "phone":  fake.phone_number(),
                "birth":  fake.date_of_birth().isoformat()
                })
        
        return {"users": users}

    @staticmethod
    def generate_posts(count: int):
        posts = []
        for _, idx in enumerate(range(count)):
            posts.append({"user_id": random.randrange(0, count), "post_id": idx, "post": fake.post(size="medium")})
        return posts

    @staticmethod
    def gen_comments(count: int):
        comments = []
        for _, idx in enumerate(range(count)):
            comments.append(
                    {"post_id": random.randrange(count),
                     "comment_id": idx,
                     "user_id": random.randrange(count),
                     "comment": fake.post(size="small")})
        return comments


def gen_fake_data(count: int):
    return {
            **Generators.generate_users(count),
            "posts": Generators.generate_posts(count),
            "comments": Generators.gen_comments(count) }
        

if __name__ == "__main__":
    out_data = json.dumps(gen_fake_data(200))
    print(out_data)
