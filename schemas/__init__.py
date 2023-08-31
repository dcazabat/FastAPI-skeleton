from pydantic import BaseModel
from datetime import datetime
from typing import Text
from uuid import uuid4

# For Users

class User(BaseModel):
    id: str
    name: str
    firstName: str
    lastName: str
    email: str
    password: str
    deleted: bool = False

class Task(BaseModel):
    id: str = str(uuid4)
    id_user: str
    title: str
    summary: Text
    dateIni: datetime = datetime.now()
    dateEnd: datetime
    completed: bool = False
    deleted: bool = False