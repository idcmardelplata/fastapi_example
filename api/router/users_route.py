from api import APIRouter, status, HTTPException, Depends, OAuth2PasswordRequestForm, RedirectResponse, JSONResponse , uuid4 , BaseModel, Annotated
from servicios.memo_storage import UserMemoStorage
from servicios.usercrudservice import CreateUser
from servicios.userauth import Login
from api.tokens.utils import (
        get_hashed_password,
        create_access_token,
        create_refresh_token,
        verify_password
        )


user_route = APIRouter(prefix="/users", tags=["users"])

class NewUser(BaseModel):
    email: str
    password: str
    user_id: str

class UserAuth(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

db = UserMemoStorage()


@user_route.post("/signup", summary="Create new user")
async def create_user(data: UserAuth):
    serv = CreateUser(data, db)

    if serv.already_exists():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists madafaka")
    else:
        serv.create()
        return JSONResponse(content={'message':'User created. Can get loged in now !'})

@user_route.post("/login", summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    serv = Login(form_data,db)

    if serv.exists_user() is False: #Verifica el usuario
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
                )
    
    
    if serv.is_pass_right() is False:
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
                )

    tokens = serv.get_tokens()
    return JSONResponse(content="{'message':'User loged. Can get into in!'}]", headers=tokens)



@user_route.get("/")
async def get_users():
    return {"msg": "Not implemented"}

