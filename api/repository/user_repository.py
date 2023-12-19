from api.schemas import User
from uuid import uuid4

class UserRepository:
    def __init__(self) -> None:
        self._db = []

    def add(self, user: User):
        self._db.append({
            "user_id": uuid4().__str__(),
            "email": user.email,
            "password": user.password
            })

    def get_user_by_email(self, email: str) -> dict[str, str] | None:
        user =  list(filter(lambda user: user["email"] == email, self._db))
        if not len(user) == 0:
            return user.pop()
        return None

    def get_user_by_id(self, user_id: str):
        # users =  list(filter(lambda user: user["user_id"] == user_id, self._db))
        # if not len(users) == 0:
        #     return users.pop()["user_id"]
        for user in self._db:
            if user["user_id"] == user_id:
                return user
            else:
                return None



    def get_all_users_by_id(self):
        ids = []
        for user in self._db:
            ids.append(user["user_id"])
        return ids



