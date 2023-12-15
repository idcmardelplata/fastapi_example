from api.tokens.tokens_managment import create_access_token, create_refresh_token
import jwt
"""administracion de tokens del sistema"""

def test_managment_should_create_access_token():
    token =  create_access_token("cifrated payload",key="key",expires_delta=10)
    decoded_data = jwt.decode(jwt=token,
                              key='key',
                              algorithms=["HS256"])
    assert decoded_data["sub"] == "cifrated payload"
    assert decoded_data["exp"] is not None
    
    
