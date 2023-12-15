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


    def exists(self,email:str) -> bool:
        return not [usuario for usuario in self._all if usuario["email"] == email] ==  []

    def get(self,email:str):
        if self.exists(email) is not False:
            return [usuario for usuario in self._all if usuario["email"] == email][0] 

    def remove(self,user_email:str):
        if self.exists(user_email):
            for index,user in enumerate(self._all): 
                if user["email"] == user_email:
                    self._all.pop(index)

    def update(self,user_email:str,updated:dict):
        outdated = self.get(user_email) 
        if outdated is not None:
            self.remove(user_email)
            self.save(updated)  
            
 
