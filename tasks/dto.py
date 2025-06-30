from pydantic import BaseModel
from datetime import datetime
from typing import Text
import uuid

class CreateTaskIn(BaseModel):
    id_user: str = str(uuid.uuid4())
    title: str
    summary: Text

class TaskOut(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str
    title: str
    summary: Text
    dateIni: datetime = datetime.now()
    dateEnd: datetime = datetime(1900, 1, 1, 0, 0, 0)
    completed: bool = False

class UpdateTask(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str = str(uuid.uuid4())
    title: str
    summary: Text

class CompletedTask(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str = str(uuid.uuid4())
    dateEnd: datetime = datetime.now()
    completed: bool = True
    
class DeletedTask(BaseModel):
    id: str = str(uuid.uuid4())
    id_user: str = str(uuid.uuid4())
    deleted: bool = True