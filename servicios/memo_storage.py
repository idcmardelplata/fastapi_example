from entidades.users import UserAuth
"""Modulo de gestion de almacenamiento en memoria"""

class UserMemoStorage:

    def __init__(self):
        self._all = []

    def get_all(self) -> list[dict]:
        return self._all

    def save(self,user:UserAuth):
        if user is not None:
            self._all.append(user)
