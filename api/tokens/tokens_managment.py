import os
from datetime import datetime, timedelta, timezone
from typing import Union, Any
import jwt


ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "LLAVESUPERSECRETA"  #Podes generar una llave segura con el comando: openssl rand -hex 32
JWT_REFRESH_SECRET_KEY = "CARGAESTODESDEUNAVARIABLEDEENTORNO-raton"

def get_exp(expires_delta:int,type:str):
    if expires_delta is not None:
        expires_delta =  datetime.now(tz=timezone.utc) + timedelta(expires_delta)
    else:
        proper_exp = None
        if type=="access":
            proper_exp = ACCESS_TOKEN_EXPIRE_MINUTES
        elif type == "refresh":
            proper_exp = REFRESH_TOKEN_EXPIRE_MINUTES
        expires_delta = datetime.utcnow() + timedelta(minutes=proper_exp)
    return expires_delta

def create_auth_token(subject: Union[str, Any], expires_delta: int = None,key="hola123",type="access") -> str:
    expires_delta = get_exp(expires_delta,type)
    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, key=key, algorithm="HS256")
    return encoded_jwt
    


