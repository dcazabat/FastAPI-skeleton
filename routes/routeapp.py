from fastapi import APIRouter
from fastapi import HTTPException

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