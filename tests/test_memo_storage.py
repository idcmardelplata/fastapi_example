from servicios.memo_storage import UserMemoStorage

def test_user_memo_storage_should_has_a_get_method_which_returns_existing_users():
    users = UserMemoStorage().get_all()
    assert type(users) is dict
