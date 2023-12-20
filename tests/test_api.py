from fastapi.testclient import TestClient
from api.server import app
import pytest


@pytest.mark.integration
def test_should_create_a_new_user():
    client =  TestClient(app)
    user_data = {
            "email": "idcmardelplata@gmail.com",
            "password": "salvenalaspapas123"
            }
    response = client.post("/users/signin",
                            json=user_data)
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "user added sucefully"}

@pytest.mark.integration
def test_create_new_user_should_fail_with_empty_password():
    client =  TestClient(app)
    user_data = {
            "email": "idcmardelplata@gmail.com",
            "password": ""
            }
    response = client.post("/users/signin",
                            json=user_data)
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": f"error on register {user_data['email']}"}

@pytest.mark.integration
def test_login():
    client =  TestClient(app)
    user_data = {
            "email": "idcmardelplata@gmail.com",
            "password": "salvenalaspapas123"}

    response = client.post("/users/signin", json=user_data)

    assert response.status_code == 200, response.text

    login = {
            "username": "idcmardelplata@gmail.com",
            "password": "salvenalaspapas123"}

    response = client.post("/users/login",
                           data=login,
                           headers={"Content-Type": "application/x-www-form-urlencoded"},
                           allow_redirects=True)

    assert response.status_code == 200, response.text
    data = response.json()
    assert type(data["auth_token"]) is str
    assert type(data["refresh_token"]) is str

