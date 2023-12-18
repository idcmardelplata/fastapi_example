from api.repository.user_repository import UserRepository, User

def test_should_store_user_into_storage():
    repo = UserRepository()
    user = User(email="idcmardelplata@gmail.com", password= "saquenalosñoquis123")
    repo.add(user)

    sut = repo.get_user_by_email("idcmardelplata@gmail.com")
    assert sut["email"] == "idcmardelplata@gmail.com"
    assert sut["password"] == "saquenalosñoquis123"
