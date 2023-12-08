import os
from datetime import datetime, timedelta
from typing import Union, Any
import bcrypt
import jwt

#TODO: Tarea para josu ;)
"""
Identificar las responsabilidades de este archivo y refactorizarlo, las tareas incluyen:
    1. Cubrir la funcionalidad de este fichero con una/s prueba/s de integracion (para asegurarse de no romper nada).
    2. Quitar la duplicación de codigo.
    3. Crear la cantidad de sub-componentes necesarios (plus si tienen test unitarios).
    4. Unir los sub-componentes creados en un componente logico (nombrarlo acorde a la funcionalidad que proporciona)
    5. Cargar los datos de JWT_SECRET_KEY y JWT_REFRESH_SECRET_KEY desde variables de entorno.
    6. Crear minimamente un endpoint que requiera autenticacion para poder acceder.
"""



ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "LLAVESUPERSECRETA"  #Podes generar una llave segura con el comando: openssl rand -hex 32
JWT_REFRESH_SECRET_KEY = "CARGAESTODESDEUNAVARIABLEDEENTORNO-raton"
SALT=bcrypt.gensalt()

def get_hashed_password(password: str):
    password_to_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_to_bytes, SALT)

def verify_password(password: str, hashed_password: bytes) -> bool:
    password_to_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_to_bytes, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    #FIXME: cambiar lo hardcodeado por variables de entorno y verificar que realmente se lean
    encoded_jwt = jwt.encode(to_encode, key="hola123", algorithm="HS256")
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes = REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": subject}

    #FIXME: cambiar lo hardcodeado por variables de entorno y verificar que realmente se lean
    encoded_jwt = jwt.encode(to_encode, "hola123", "HS256")
    # encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
