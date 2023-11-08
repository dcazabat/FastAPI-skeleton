from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.users import User, UpdateUser, CreateUserOut, CreateUserIn, GetUser, LoginUser
from services.userdb import createUserDB, getUserDB, getUsers, updateUserDB, deleteUserDB, loginUser
from middlewares.auth import create_access_token
from typing import List

user = APIRouter()

# Method for Users
@user.get('', response_model=List[GetUser], status_code=200)
async def get_all_users():
    # Send all users
    # try:
        users = getUsers()
        if users:
            return users
        # If not found, return 404
        return JSONResponse(status_code=404, content=f'Users: not found')
        # raise HTTPException(status_code=404, detail=f'Users: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting users: {e}")
    
@user.get('/{id}', response_model=GetUser, status_code=200)
async def get_user(id: str):
    # Check if users exists
    try:
        user = getUserDB(id=id)
        if user:
            return user
        return JSONResponse(status_code=404, content={'message' : f'User: {id} not found'})
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting user {id}: {e}")

@user.post('', response_model=CreateUserOut, status_code=200)
async def create_user(user: CreateUserIn):
    try:
        newUser = createUserDB(user=user)
        if newUser:
            newUserDict = jsonable_encoder(CreateUserOut(**jsonable_encoder(newUser)))
            return JSONResponse(status_code=200, content={'message': 'User Create OK', 'data': newUserDict})
        return JSONResponse(status_code=404, content={'message': 'User NOT Create'})
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: User creation failed: {e}")

@user.put('/{id}', response_model=UpdateUser, status_code=200)
async def update_user(id: str, user: UpdateUser):
    try:
        updatedUser = updateUserDB(id=id, updated_user=user)
        if updatedUser:
            updatedUserDict = jsonable_encoder(updatedUser)
            return JSONResponse(status_code=200, content={'message': 'User Update OK', 'data': updatedUserDict})
        return JSONResponse(status_code=404, content={'message': 'User NOT Update'})
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for User ID: {id}, Error {e}")

@user.delete('/{id}', response_model=User, status_code=200)
async def delete_user(id: str):
    try:
        deleteUser = deleteUserDB(id=id)
        if deleteUser:
            return deleteUser
        raise HTTPException(status_code=404, detail=f'User: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Delete Failed for User ID: {id}, Error {e}")

@user.post('/login',response_model=dict, status_code=200)
async def login_user(user: LoginUser):
    # Falta devolver el token
    try:
        userOK = loginUser(user=user)
        if userOK:
            data = { 'username': userOK.name,
                     'id': userOK.id}
            token = create_access_token(data=data)
            return JSONResponse(status_code=200, content={'token': token})
        return JSONResponse(status_code=404, content={'message': 'User Not Authenticate'})
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Server Error for User: {user.name}, Error {e}")