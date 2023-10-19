from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

class LoginUser(BaseModel):
    name: str
    password: str

class CreateUserOut(BaseModel):
    id: str
    name: str
    firstName: str
    lastName: str
    email: str
    password: str

class CreateUserIn(BaseModel):
    name: str
    firstName: str
    lastName: str
    email: str
    password: str

class GetUser(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    firstName: str
    lastName: str
    email: str

class User(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    firstName: str
    lastName: str
    email: str
    password: str
    deleted: bool = False

class UpdateUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
