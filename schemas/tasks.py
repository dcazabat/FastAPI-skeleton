from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

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
    dateEnd: datetime = datetime(1900, 1, 1, 0, 0, 0)
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