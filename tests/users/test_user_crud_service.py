from fastapi.testclient import TestClient
from servicios.users.account.crud import CreateUser
from servicios.memo_storage import UserMemoStorage
from entidades.users import UserAuth

class user_data:
    def __init__(self):
        self.email:str = None
        self.password:str = None

def test_create_user_uses_memo_storage_is_saving():
    db = UserMemoStorage()
    data = user_data()
    data.email = "jose.s.contacto@gmail.com"
    data.password = "VivaLaLibertadCarajo123"
    sut = CreateUser(data, db)
    assert len(sut._db._all) == 0
    sut.create()
    assert len(sut._db._all) > 0
    

    
