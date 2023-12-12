"""Modulo de gestion de almacenamiento en memoria"""

class UserMemoStorage:

    def __init__(self):
        self._all = {}

    def get_all(self) -> list[dict]:
        return self._all
