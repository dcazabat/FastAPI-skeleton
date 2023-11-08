from fastapi import APIRouter
from fastapi import HTTPException
from schemas import User, UpdateUser, CreateUser
from methods.userdb import createUserDB, getUserDB, getUsers, updateUserDB, deleteUserDB

user = APIRouter()

# Method for Users
@user.get('', response_model=list[User], tags=['Users'])
async def get_all_users():
    # Send all users
    # try:
        users = getUsers()
        if users:
            return users
        print('Routes')
        raise HTTPException(status_code=204, detail=f'Users Empty')    
    # except Exception as e:
    #     return e
        # raise HTTPException(status_code=500,detail=f"Error getting users: {e}")
    
@user.get('/{id}', response_model=User, tags=['Users'])
async def get_user(id: str):
    # Check if users exists
    try:
        user = getUserDB(id=id)
        if user:
            return user
        raise HTTPException(status_code=404, detail=f'User: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting user {id}: {e}")

@user.post('', response_model=CreateUser, tags=['Users'])
async def create_user(user: CreateUser):
    try:
        new_user = createUserDB(user=user)
        print(new_user)
        return new_user
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: User creation failed: {e}")

@user.put('/{id}', response_model=UpdateUser, tags=['Users'])
async def update_user(id: str, user: UpdateUser):
    try:
        updatedUser = updateUserDB(id=id, updated_user=user)
        if updatedUser:
            return updatedUser
        raise HTTPException(status_code=404, detail=f'User: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for User ID: {id}, Error {e}")

@user.delete('/{id}', response_model=User, tags=['Users'])
async def delete_user(id: str):
    try:
        deleteUser = deleteUserDB(id=id)
        if deleteUser:
            return deleteUser
        raise HTTPException(status_code=404, detail=f'User: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Delete Failed for User ID: {id}, Error {e}")
