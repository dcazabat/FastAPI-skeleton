from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from uuid  import uuid4

# Local imports
from schemas import User
from config import users


user = APIRouter()

#Method for Users
@user.get('', tags=['Users'])
async def get_all_users():
    from pprint import pprint
    # Send all users
    pprint(users)
    users_dict = {}
    if users.__len__() > 0:
        for user in users:
            if user['deleted'] == False:
                users_dict[user['id']] = user
        if users_dict.__len__() > 0:
            return users_dict
    # If not found, return 404
    raise HTTPException(status_code=404, detail=f'Users: not found')

@user.get('/{id}', response_model=User, tags=['Users'])
async def get_user(id: str):
    # Check if users exists
    if users.__len__() > 0:
        # Search for user in database
        user_find = [ user for user in users if user['id'] == id and user['deleted'] == False ]
        if user_find.__len__() > 0:
            return user_find[0]
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'user: {id} not found')
    # If not found, return 404
    raise HTTPException(status_code=404, detail='Users: not found')

@user.post('', response_model=User, tags=['Users'])
async def create_user(user: User):
    user.id = str(uuid4())
    users.append(jsonable_encoder(user))
    return user

@user.put('/{id}', response_model=User, tags=['Users'])
async def update_user(id: str, user: User):
    # Check if users exists
    if users.__len__() > 0:
        # Search for user in database
        user_find = next((i for i, user in enumerate(users) if user["id"] == id and user['deleted'] == False), None)
        if user_find != None:
            print(jsonable_encoder(user))
            user.id = id # This line should not be there because the "user" parameter contains all the data in addition to the modified ones.
            users[user_find] = jsonable_encoder(user)
            return users[user_find]
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'user: {id} not found')
    # If not found, return 404
    raise HTTPException(status_code=404, detail='Users: not found')

@user.delete('/{id}', response_model=User, tags=['Users'])
async def delete_user(id: str):
    # Check if users exists
    if users.__len__() > 0:
        # Search for user in database
        user_find = next((i for i, user in enumerate(users) if user["id"] == id and user['deleted'] == False), None)
        if user_find != None:
            users[user_find].deleted = not users[user_find].deleted
            return users[user_find]
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'user: {id} not found')
    # If not found, return 404
    raise HTTPException(status_code=404, detail='Users: not found')