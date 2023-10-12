from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Text, Boolean, DateTime
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

import uuid
from datetime import datetime

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    firstName = Column(String(100))
    lastName = Column(String(100))
    email = Column(String(100))
    password = Column(String(100), nullable=False)
    deleted = Column(Boolean, default=False)
    tasks = relationship('TaskDB', backref='users', lazy=True)
   
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, firstname={self.firstName!r}, lastname={self.lastName!r})"

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    title = Column(String(80), nullable=False)
    summary = Column(Text, nullable=False)
    dateIni = Column(DateTime, nullable=False, default= datetime.now())
    dateEnd = Column(DateTime)
    completed = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    id_user = Column(String(50), ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, id_user={self.id_user!r}, title={self.title!r}, summary={self.summary!r}, completed={self.completed!r})"

class Test(Base):
    __tablename__ = "jorge"
    id = Column(String(20), primary_key=True)