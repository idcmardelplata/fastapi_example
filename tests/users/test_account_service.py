from servicios.users.userservice import AccountService

def test_account_service_should_has_a_crud_module():
    assert AccountService().crud is not None

def test_account_service_should_has_a_sessions_module():
    assert AccountService().sessions is not None
