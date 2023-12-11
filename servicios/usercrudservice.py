from api.tokens.utils import get_hashed_password
from uuid import uuid4

class CreateUser:

    def __init__(self,data,db):
        self._data = data
        self._db = db
        self._user = db.get(data.email, None)

    def already_exists(self):
        if self._user is not None:
            return True

    def create(self):
        user = {
                'email': self._data.email,
                'password': get_hashed_password(self._data.password),
                'user_id': str(uuid4())
                }

        self._db[self._data.email] = user #guarda el usuario en la base de datos
        


        


