from api.schemas import User
from uuid import uuid4

class UserRepository:
    def __init__(self) -> None:
        self._db = []

    def add(self, user: User):
        self._db.append({
            "id": uuid4().int,
            "email": user.email,
            "password": user.password
            })

    def get_user_by_email(self, email: str) -> dict[str, str] | None:
        user =  list(filter(lambda user: user["email"] == email, self._db))
        if not len(user) == 0:
            return user.pop()
        return None

