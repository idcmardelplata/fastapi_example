# from fastapi.testclient import TestClient
# from api.server import app
# import pytest
#
# client = TestClient(app)

# @pytest.mark.integration
# def test_should_create_a_new_user():
#     response = client.post("/users/signin",
#                            json={"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"})
#     assert response.status_code == 200
#     assert response.json() == {"msg": "user added sucefully"}

# @pytest.mark.integration
# def test_unprotected_route_can_by_access_for_non_authenticated_users():
#     response = client.get("/posts")
#     assert response.status_code == 200
#     assert type(response.json()) is list
#     assert len(response.json()) == 100
#
# @pytest.mark.integration
# def test_protected_route():
#     # Make new user
#     response = client.post("/users/signin",
#                             json={"email": "idcmardelplata@gmail.com", "password": "salvenalaspapas123"})
#     assert response.status_code == 200
#     assert response.json() == {"msg": "user added sucefully"}
#
#     response = client.post("/users/login",
#                            content={'email': 'idcmardelplata@gmail.com', 'password': 'clave123'})
#
#     assert type(response.json()) is dict
#
#     data = response.json()
#     assert data == {"msg": "Incorrect email or password"}
#     # auth_token =  data["msg"]["Loggin sucess"]["auth_token"]
#     # refresh_token = data["msg"]["Loggin sucess"]["refresh_token"] 
#
#     # assert auth_token != refresh_token








    # response = client.get("/comments", headers={'Autorization: Bearer': auth_token})
