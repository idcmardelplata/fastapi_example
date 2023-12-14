class AuthService:
    pass

class SessionService:
    def __init__(self,auth=AuthService()):
        self.auth=auth

class Crud:
    pass

class AccountService:
    def __init__(self,crud=Crud(),sessions=SessionService()):
        self.crud = crud
        self.sessions = sessions

class UserService:
    def __init__(self,account=AccountService()):
        self.accounts = account

