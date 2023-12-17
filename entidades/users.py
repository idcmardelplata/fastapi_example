from pydantic import BaseModel

# FIX: Esto no es una entidad
"""
acordate que una entidad debe tener una identificacion propia, esto es mas bien un modelo.
"""
class UserAuth(BaseModel):
    email: str
    password: str
