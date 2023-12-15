import os
from datetime import datetime, timedelta, timezone
from typing import Union, Any
import jwt


ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "LLAVESUPERSECRETA"  #Podes generar una llave segura con el comando: openssl rand -hex 32
JWT_REFRESH_SECRET_KEY = "CARGAESTODESDEUNAVARIABLEDEENTORNO-raton"


def create_access_token(subject: Union[str, Any], expires_delta: int = None, key="hola123") -> str:
    if expires_delta is not None:
        expires_delta =  datetime.now(tz=timezone.utc) + timedelta(expires_delta)
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    #FIXME: cambiar lo hardcodeado por variables de entorno y verificar que realmente se lean
    encoded_jwt = jwt.encode(to_encode, key=key, algorithm="HS256")
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None,key="hola123") -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes = REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": subject}

    #FIXME: cambiar lo hardcodeado por variables de entorno y verificar que realmente se lean
    encoded_jwt = jwt.encode(to_encode, key=key, algorithm="HS256")
    # encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
