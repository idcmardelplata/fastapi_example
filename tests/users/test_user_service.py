from servicios.users.userservice import UserService

def test_user_service_should_has_a_account_component():
    assert UserService().accounts is not None


