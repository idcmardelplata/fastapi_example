from api.account import Account, LogginResult
from api.schemas import User
from generators import gen_random_user, gen_registered_user


#TODO: The user not should exists

def test_should_register_new_user():
    user = gen_random_user()
    account = Account()

    assert account.register(user) == True

    assert account.login(user) != {"msg": "incorrect email or password"}
    
def test_login():
    account, user = gen_registered_user()
    response = account.login(user)

    assert type(response) is LogginResult
    assert response != {"msg": "incorrect email or password"}

def test_logout():
    account, user = gen_registered_user()
    response = account.logout(user)
    assert response == {"msg": "user logout"}

