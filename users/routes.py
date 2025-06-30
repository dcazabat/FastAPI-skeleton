from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from users.dto import *
from users.services import *
from middlewares.auth import create_access_token
from typing import List

user = APIRouter()

# Method for Users
@user.get('', response_model=List[UserOut], status_code=200)
async def get_all_users():
    # Send all users
    try:
        users = getUsers()
        if users:
            return users
        # If not found, return 404
        return JSONResponse(status_code=404, content=f'Users: not found')
        # raise HTTPException(status_code=404, detail=f'Users: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting users: {e}")
    
@user.get('/{id}', response_model=UserOut, status_code=200)
async def get_user(id: str):
    # Check if users exists
    try:
        user = getUser(id=id)
        if user:
            return user
        return JSONResponse(status_code=404, content={'message' : f'User: {id} not found'})
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting user {id}: {e}")

@user.post('', response_model=UserOut, status_code=200)
async def create_user(user: CreateUserIn):
    try:
        print(user)
        newUser = createUser(user=user)
        if newUser:
            return newUser
        return JSONResponse(status_code=404, content={'message': 'User NOT Create'})
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: User creation failed: {e}")

@user.put('', response_model=UserOut, status_code=200)
async def update_user(user: UpdateUser):
    try:
        updUser = updateUser(user=user)
        if updUser:
            return updUser
        return JSONResponse(status_code=404, content={'message': 'User NOT Update'})
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for User, Error {e}")

@user.delete('', response_model=UserOut, status_code=200)
async def delete_user(user: DeleteUser):
    try:
        delUser = deleteUser(user=user)
        if delUser:
            return delUser
        return JSONResponse(status_code=404, content={'message': 'User NOT Delete'})
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Delete Failed for User, Error {e}")

@user.post('/login',response_model=dict, status_code=200)
async def login_user(user: LoginUser):
    # Falta devolver el token
    try:
        userOK = loginUser(user=user)
        print(userOK)
        if userOK:
            data = { 'username': userOK.name, 'id': userOK.id}
            token = create_access_token(data=data)
            return JSONResponse(status_code=200, content={'token': token})
        return JSONResponse(status_code=404, content={'message': 'User Not Authenticate'})
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Server Error for User, Error {e}")