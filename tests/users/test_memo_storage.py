from servicios.memo_storage import UserMemoStorage

def test_user_memo_storage_should_has_a_get_method_which_returns_existing_users():
    users = UserMemoStorage().get_all()
    assert type(users) is list


def test_user_memo_storage_should_has_a_save_method_which_stores_users():
    storage = UserMemoStorage()
    storage.save({
        "email": "julian@gmail.com",
        "password": "superpass123"
    })
    user = storage.get_all()[0]
    assert user["email"] == "julian@gmail.com"
    assert user["password"] == "superpass123"

def test_user_memo_storage_should_has_a_exists_method():
    storage = UserMemoStorage()
    storage.save({
        "email": "julian@gmail.com",
        "password": "superpass123"
    })
    assert storage.exists("julian@gmail.com")

def test_user_memo_should_update_user():
    storage = UserMemoStorage()
    access_token = "123supercalifragilisticoespialidoso"
    storage.save({
        "email": "julian@gmail.com",
        "password": "superpass123"
    })
    storage.update("julian@gmail.com",updated={
        "email": "julian@gmail.com",
        "password": "superpass123",
        "access_token":access_token
    })
    assert storage.get("julian@gmail.com")["access_token"]==access_token

