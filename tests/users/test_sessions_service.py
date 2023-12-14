from servicios.users.userservice import SessionService

def test_sessions_service_should_has_auth_module():
    assert SessionService().auth is not None
