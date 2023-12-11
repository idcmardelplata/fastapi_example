from api.tokens.utils import verify_password,create_access_token,create_refresh_token

class Login:

    def __init__(self,form_data,db):
        self._form_data= form_data
        self._db = db
        self._user = self._db.get(form_data.username, None)

    def exists_user(self):
        return self._user is not None

    def is_pass_right(self):
        hashed_pass = self._user["password"]
        return verify_password(self._form_data.password, hashed_pass) #Verifica la contraseña
    
    def get_tokens(self) -> list:
        return {
            "access_token": create_access_token(self._user["email"]), 
            "refresh_token": create_refresh_token(self._user["email"])
        }

