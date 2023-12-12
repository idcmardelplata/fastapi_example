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

