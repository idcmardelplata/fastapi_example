from servicios.password_managment import get_hashed_password
from servicios.memo_storage import UserMemoStorage
from uuid import uuid4

class CreateUser:

    def __init__(self,data,db=UserMemoStorage()):
        self._data = data
        self._db = db

    def already_exists(self):
        return self._db.exists(self._data.email)

    def create(self):
        user = {
                'email': self._data.email,
                'password': get_hashed_password(self._data.password),
                'user_id': str(uuid4())
                }

        self._db.save(user)


