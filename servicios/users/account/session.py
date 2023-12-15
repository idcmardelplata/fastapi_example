from api.tokens.tokens_managment import create_auth_token
from servicios.users.account.passman import verify_password
from servicios.memo_storage import UserMemoStorage
from servicios.users.account.auth import AuthService

class SessionService:
    def __init__(self,auth=AuthService()):
        self.auth=auth


class Login:

    def __init__(self,form_data,db=UserMemoStorage):
        self._form_data= form_data
        self._db = db
        self._user = self._db.get(form_data.username)

    def exists_user(self):
        return self._user is not None

    def is_pass_right(self):
        hashed_pass = self._user["password"]
        return verify_password(self._form_data.password, hashed_pass) #Verifica la contraseña
    
    def get_tokens(self) -> list:
        return {
            "access_token": create_auth_token(self._user["email"],type="access"), 
            "refresh_token": create_auth_token(self._user["email"],type="refresh")
        }


