from fastapi.testclient import TestClient
from api.server import app
import pytest

# @pytest.fixture(scope="module")
# def client():
#     with TestClient(app) as c:
#       yield c
#
# @pytest.fixture(scope="module")
# def test_user():
#     return {"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"}


# def test_login(client, test_user):
#   response = client.post("/users/login", data=test_user)
#   assert response.status_code == 200
#   token = response.json()["access_token"]
#   assert token is not None
#   return token
#

client = TestClient(app)


# TODO: Mark this as integration test
def test_should_create_a_new_user():
    response = client.post("/users/signin",
                           json={"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"})
    assert response.status_code == 200
    assert response.json() == {"msg": "user added sucefully"}
#
# def test_should_login_a_user():
#     client.post("/users/signin",
#                            json={"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"})
#
#     response = client.post("/users/login",
#                            params={"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"})
#     assert response.status_code == 200
#     assert response.json() == {"msg": "user added sucefully"}
#
