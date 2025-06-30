from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

class LoginUser(BaseModel):
    name: str
    password: str

class CreateUserIn(BaseModel):
    name: str
    firstName: str
    lastName: str
    email: str
    password: str

class UserOut(BaseModel):
    id: str
    name: str
    firstName: str
    lastName: str
    email: str

class DeleteUser(BaseModel):
    id: str = str(uuid.uuid4())
    deleted: bool = False

class ChangePassword(BaseModel):
    id: str = str(uuid.uuid4())
    password: str
    
class UpdateUser(BaseModel):
    id: str = str(uuid.uuid4())
    firstName: str
    lastName: str
    email: str
