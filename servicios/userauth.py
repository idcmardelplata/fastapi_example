from api.tokens.utils import verify_password,create_access_token,create_refresh_token

class Login:

    def __init__(self,form_data,db):
        self._form_data= form_data
        self._db = db
        self._user = self._db.get(form_data.username, None)

    def exists_user(self):
        if self._user is None: 
            return False

    def is_pass_right(self):
        hashed_pass = self._user["password"]
        if not verify_password(form_data.password, hashed_pass): #Verifica la contraseña
            return False
    
    def get_tokens(self) -> list:
        accs_tok = create_access_token(self._user["email"])
        refrh_tok = create_refresh_token(self._user["email"])
        return {"access_token": accs_tok, "refresh_token": refrh_tok }

