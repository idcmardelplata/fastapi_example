from api.account import Account
from api.schemas import User
from generators import gen_random_user, gen_registered_user


#TODO: The user not should exists

def test_should_register_new_user():

    user = gen_random_user()
    account = Account()
    assert account.register(user) == True

    sut = account.get_user_by_email(user.email)

    assert sut["email"] == user.email
    assert sut["password"] != user.password
    
def test_login():
    account, user = gen_registered_user()
    response = account.login(user)

    assert type(response) == dict
    assert response != {"msg": "incorrect email or password"}
