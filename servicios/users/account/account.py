
from servicios.users.account.crud import Crud
from servicios.users.account.session import SessionService
import servicios.users.account.passman as passman

class AccountService:
    def __init__(self,crud=Crud(),sessions=SessionService()):
        self.crud = crud
        self.sessions = sessions
        self.passman = passman




