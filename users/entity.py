from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Text, Boolean, DateTime
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from default.basemodel import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default='')
    name = Column(String(100), nullable=False)
    firstName = Column(String(100))
    lastName = Column(String(100))
    email = Column(String(100))
    password = Column(String(100), nullable=False)
    deleted = Column(Boolean, default=False)
    tasks = relationship('Task', backref='users', lazy=True)
   
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, firstname={self.firstName!r}, lastname={self.lastName!r})"