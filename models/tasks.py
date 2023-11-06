from sqlalchemy import ForeignKey
from sqlalchemy import String, Text, Boolean, DateTime
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from services.cnx import Base

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(String(50), primary_key=True, default="")
    title = Column(String(100), nullable=False)
    summary = Column(Text, nullable=False)
    dateIni = Column(DateTime, nullable=False)
    dateEnd = Column(DateTime, nullable=False)
    completed = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    id_user = Column(String(50), ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, id_user={self.id_user!r}, title={self.title!r}, summary={self.summary!r}, completed={self.completed!r})"