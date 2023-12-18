import os
import bcrypt
from api.repository.user_repository import UserRepository
from api.account.auth import create_tokens
from api.schemas import User
from dotenv import load_dotenv

class Account:

    def __init__(self) -> None:
        self.repo = UserRepository()
        load_dotenv()

    def register(self, user: User) -> bool:
        hashed_password = bcrypt.hashpw(user.password.encode(), salt=bcrypt.gensalt())

        user = User(**{"email": user.email, "password": hashed_password})

        self.repo.add(user)
        return True

    def get_user_by_email(self, email: str):
        return self.repo.get_user_by_email(email)

    def login(self, user: User):
        #TODO: Debo almacenar el refresh token en una db
        stored_user = self.repo.get_user_by_email(user.email)
        if stored_user is None:
            return {"msg": "incorrect email or password"}
        else:
            if bcrypt.checkpw(user.password.encode('utf-8'), hashed_password=stored_user["password"].encode('utf-8')):
                tokens = create_tokens(stored_user["id"])
                return {"msg": {"Loggin sucess": tokens}}

