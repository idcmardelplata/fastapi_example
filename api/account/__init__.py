import bcrypt
from api.repository import UserRepository, RefreshTokenRepository
from api.account.auth import create_tokens, read_token, create_auth_token
from api.schemas import User
from dotenv import load_dotenv

class Account:

    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.refresh_token_repository = RefreshTokenRepository()

        load_dotenv()

    def register(self, user: User) -> bool:
        if self._validate_data(user):
            hashed_password = bcrypt.hashpw(user.password.encode(), salt=bcrypt.gensalt())

            user = User(**{"email": user.email, "password": hashed_password})

            self.user_repository.add(user)
        #NOTE: Optional could return an auth token 
            return True
        return False

    def login(self, user: User):
        stored_user = self.user_repository.get_user_by_email(user.email)
        if stored_user is None:
            return {"msg": "incorrect email or password"}
        else:
            if bcrypt.checkpw(user.password.encode('utf-8'), hashed_password=stored_user["password"].encode('utf-8')):
                tokens = create_tokens(stored_user["user_id"])
                self.refresh_token_repository.add_refresh_token(user.email, tokens["refresh_token"])
                #FIX: cambiar esto para que retorne solamente los tokens en un diccionario
                return {"msg": {"Loggin sucess": tokens}}

    def exists_refresh_token(self, token: str) -> bool:
        return self.refresh_token_repository.refresh_token_exists(token)

    def logout(self, user: User):
        self.refresh_token_repository.delete_token(user.email)
        return {"msg": "user logout"}

    def read_refresh_token(self, refresh_token: str):
        return read_token(refresh_token, token_type="refresh")

    def read_auth_token(self, auth_token: str):
        return read_token(auth_token, token_type="auth")

    def create_auth_token(self, user_id: str):
        return create_auth_token(user_id)

    def get_user_by_id(self, user_id: str):
        return self.user_repository.get_user_by_id(user_id=user_id)

    def get_all_users_by_id(self):
        return self.user_repository.get_all_users_by_id()

    def _validate_data(self, user: User):
        #HACK: Should use pydantic validation for that!!
        return len(user.email) > 10 and len(user.password) > 8
