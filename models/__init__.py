from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Text, Boolean, DateTime
from sqlalchemy import Column

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import ForeignKey

from uuid import uuid4
from datetime import datetime

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"
    id: Column(String(100), primary_key=True, default=str(uuid4))
    name: Column(String(100), nullable=False)
    firstName: Column(String(100))
    lastName: Column(String(100))
    email: Column(String(100))
    password: Column(String(100), nullable=False)
    deleted: Column(Boolean, default=False)
    task = relationship('TaskDB', backref='users', lazy=True)
   
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, lastname={self.lastName!r}, fullname={self.fullname!r})"

class TaskDB(Base):
    __tablename__ = "tasks"
    id: Column(String(100), primary_key=True, default=str(uuid4))
    title: Column(String(100), nullable=False)
    summary: Column(Text, nullable=False)
    dateIni: Column(DateTime, nullable=False, default= datetime.now())
    dateEnd: datetime
    completed: bool = False
    deleted: bool = False
    id_user: Column(String(100), ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, id_user={self.id_user!r}, title={self.title!r}, summary={self.summary!r}, completed={self.completed!r})"