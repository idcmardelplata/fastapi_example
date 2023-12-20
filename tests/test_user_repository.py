from typing import List
from api.repository import UserRepository, User
from tests.generators import gen_random_user

def test_should_store_user_into_storage():
    repo = UserRepository()
    user = User(email="idcmardelplata@gmail.com", password= "saquenalosñoquis123")
    repo.add(user)

    sut = repo.get_user_by_email("idcmardelplata@gmail.com")
    assert sut["email"] == "idcmardelplata@gmail.com"
    assert sut["password"] == "saquenalosñoquis123"

def test_user_not_exists():
    repo = UserRepository()
    user = User(email="non-existing-user@gmail.com", password="nothing")

    sut = repo.get_user_by_email("non-existing-user@gmail.com")
    assert sut == None

def test_get_user_by_id():
    repo = UserRepository()
    user = User(email="non-existing-user@gmail.com", password="nothing")
    user_id = repo.add(user) #TODO: add debe retornar el id del usuario agregado

    assert isinstance(repo.get_user_by_id(user_id), User)
    assert type(user_id) is str

# get_user_by_id debe retornar None si no hay usuarios en la db
def test_get_user_by_id_not_found_user():
    repo = UserRepository()
    repo.add(User(email="user@gmail.com", password="password123"))
    assert repo.get_user_by_id("-") == None

def test_get_all_users_by_id():
    repo = UserRepository()
    sut = []

    for _ in range(0,3):
        sut.append(repo.add(gen_random_user()))
    assert repo.get_all_users_by_id() == sut




