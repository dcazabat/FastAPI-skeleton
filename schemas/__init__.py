from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

# For Users
class CreateUser(BaseModel):
    name: str
    firstName: str
    lastName: str
    email: str
    password: str

class User(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    firstName: str
    lastName: str
    email: str
    password: str
    deleted: bool = False

class UpdateUser(BaseModel):
    name: str
    firstName: str
    lastName: str
    email: str
    password: str


# For Tasks
class CreateTask(BaseModel):
    id_user: str
    title: str
    summary: Text

class Task(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str
    title: str
    summary: Text
    dateIni: datetime = datetime.now()
    dateEnd: datetime
    completed: bool = False
    deleted: bool = False

class UpdateTask(BaseModel):
    title: str
    summary: Text
    dateEnd: datetime
    completed: bool