from servicios.users.account.account import AccountService

class UserService:
    def __init__(self,account=AccountService()):
        self.accounts = account

