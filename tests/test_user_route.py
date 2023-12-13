from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)

def test_user_should_be_created():
    response = client.post("/users/signup",json={
          "email": "string",
          "password": "string"
    })
    assert response.json()=={'message':'User created. Can get loged in now !'}

def test_user_should_not_be_reppited():
    response = client.post("/users/signup",json={
          "email": "string",
          "password": "string"
    })
    response = client.post("/users/signup",json={
          "email": "string",
          "password": "string"
    })
    assert response.json()["detail"]=="User with this email already exists madafaka"



