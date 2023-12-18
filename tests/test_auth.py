import os
import pytest
from api.account.auth import create_token, read_token, create_tokens, InvalidTokenError

def test_given_user_id_should_return_a_auth_token():
    user_id = "356adf35d5bca05c96a878912025952a1c184c3c91be000ac345addbefb1660b"
    token = create_token(user_id, expiration_time=1, key="hola123")
    assert type(token) is str

    decoded_token_info = read_token(token, key="hola123")
    assert decoded_token_info["user_id"] == user_id

def test_should_be_fail_if_keys_not_match():
    user_id = "356adf35d5bca05c96a878912025952a1c184c3c91be000ac345addbefb1660b"
    token = create_token(user_id, expiration_time=1, key="correct-key")

    with pytest.raises(InvalidTokenError):
        read_token(token, key="wrong-key")

def test_factory_should_create_auth_and_refresh_tokens():
    user_id = "356adf35d5bca05c96a878912025952a1c184c3c91be000ac345addbefb1660b"
    os.environ["AUTH_TOKEN_KEY"] = "4f037dd30e2e0e92873194ddb7605f4987e68742bc0e67866b15dcded5e6daf2"
    os.environ["REFRESH_TOKEN_KEY"] = "e35269023e3f7bb7f7b7e53175bf4dba0ed4ebccf0d7a6ee18a16fd3d43fe042"

    tokens = create_tokens(user_id)

    auth_token = tokens["auth_token"]
    refresh_token = tokens["refresh_token"]

    refresh_data = read_token(refresh_token, token_type="refresh")
    auth_data = read_token(auth_token, token_type="auth")

    assert refresh_data["user_id"] == user_id
    assert auth_data["user_id"] == user_id

    assert refresh_data["exp"] > auth_data["exp"]

