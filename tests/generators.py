from faker import Faker
from api.schemas import User
from api.account import Account


def gen_random_user():
    faker = Faker()
    return User(email=faker.email(), password=faker.password())

def gen_registered_user():
    account = Account()
    user = gen_random_user()
    account.register(user)
    return account, user
