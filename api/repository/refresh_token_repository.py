from api.schemas import User

class RefreshTokenRepository:
    def __init__(self) -> None:
        self._db = []

    def add_refresh_token(self, email: str, token: str):
        if self.get_refresh_token(email) != {"msg": "refresh token not found"}: #Token exists into db
            self.delete_token(email)
        else:
            self._db.append({
                "email": email,
                "refresh_token": token
                })

    def get_refresh_token(self, email):
        token = list(filter(lambda record: record.email == email, self._db))
        if token:
            return token
        else:
            return {"msg": "refresh token not found"}

    def delete_token(self, email: str):
        records = list(filter(lambda record: record.email == email, self._db))
        if len(records) > 0:
            del self._db[records.pop()]


