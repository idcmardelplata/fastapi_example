from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
import os
from dotenv import load_dotenv

REFRESH_TOKEN_EXPIRATION_TIME_DAYS = (60 * 60 * 24) * 7  #7 days
load_dotenv()

def _read_token_key_from_env():
    return {"refresh": os.environ["REFRESH_TOKEN_KEY"], "auth": os.environ["AUTH_TOKEN_KEY"]}

def create_token(user_id: str, expiration_time=0, key=None, token_type="auth") -> str:
    current_date = datetime.now(tz=timezone.utc)

    if expiration_time == 0:
        expiration_time = current_date + timedelta(minutes=2)
    else:
        expiration_time = current_date + timedelta(minutes=expiration_time)

    token_key = _read_token_key_from_env()[token_type] if key==None else key

    payload = {"exp": expiration_time, "user_id": user_id}
    return jwt.encode(payload, token_key)

def read_token(token: str, key=None, token_type="auth" ):
    key = _read_token_key_from_env()[token_type] if key == None else key
    return  jwt.decode(token, key, algorithms=["HS256"])


def create_tokens(user_id: str) -> dict[str, str]:
    auth_token = create_token(user_id, token_type="auth")
    refresh_token = create_token(user_id, expiration_time=REFRESH_TOKEN_EXPIRATION_TIME_DAYS, token_type="refresh")
    return {"auth_token": auth_token, "refresh_token": refresh_token}

def create_auth_token(user_id: str) -> str:
    return create_token(user_id, expiration_time=2, token_type="auth")
