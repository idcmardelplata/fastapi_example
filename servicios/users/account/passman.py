from api import bcrypt


SALT=bcrypt.gensalt()

def get_hashed_password(password: str):
    password_to_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_to_bytes, SALT)

def verify_password(password: str, hashed_password: bytes) -> bool:
    password_to_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_to_bytes, hashed_password)

def shout():
    print("estamos en la b! ¡ESTAMOS EN LA B!")
