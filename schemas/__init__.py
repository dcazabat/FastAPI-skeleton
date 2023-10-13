from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

# For Users
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


# For Tasks
class CreateTaskIn(BaseModel):
    title: str
    summary: Text

class CreateTaskOut(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str = str(uuid.uuid4())
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

class CompletedTask(BaseModel):
    dateEnd: datetime = datetime.now()
    completed: bool = True