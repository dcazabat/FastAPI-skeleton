from fastapi import APIRouter
from fastapi import HTTPException
from schemas.users import LoginUser
from middlewares.auth import create_access_token
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

default = APIRouter()


@default.get('/')
@default.get('/home')
def root():
    # Validate if the users and passwords are correct
    return {'message': 'Hello World'}


@default.get('/test')
def test():
    resp = {'firtname': 'Jhon', 'lastname': 'Wick',
            'isdanger': 'Very High', 'age': 53}
    return resp

# @default.post("/token", response_model=dict)
# async def login_for_access_token(user: LoginUser):
#     user_data = authenticate_user(user.name, user.password)
#     if not user_data:
#         raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
#     access_token_expires = timedelta(minutes=os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
