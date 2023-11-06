from schemas.tasks import Task, UpdateTask, CreateTaskIn, CompletedTask
from models.tasks import TaskDB
from services.cnx import SessionLocal
import uuid
from datetime import datetime

# Function to get all task 
def getTasks(id_user: str):
    try:
        db = SessionLocal()
        tasks = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.deleted == False).all()
        # print(tasks)
        if tasks:
            db.close()
            return tasks
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Function to get one task
def getTaskDB(id_user: str, id: str):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()
        if task:
            db.close()
            return task
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Creation of "Task" is used in the "POST" method
def createTaskDB(id_user: str, task: CreateTaskIn):
    try:
        db = SessionLocal()
        new_task = TaskDB(
                        id=str(uuid.uuid4()),
                        id_user=id_user,
                        dateIni = datetime.now(),
                        dateEnd = datetime(1900,1,1,0,0,0),
                        title=task.title,
                        summary=task.summary,
                        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to get update the "task", used in "PUT" methods
def updateTaskDB(id_user:str,  id: str, updated_task: UpdateTask):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()

        if task:
            task.title=updated_task.title
            task.summary=updated_task.summary
            task.dateEnd=updated_task.dateEnd
            task.completed=updated_task.completed
            db.refresh(task)
            db.commit()
            db.close()
            return task
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def completTaskDB(id_user:str,  id: str, updated_task: CompletedTask):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()

        if task:
            task.dateEnd=updated_task.dateEnd
            task.completed=updated_task.completed
            db.refresh(task)
            db.commit()
            db.close()
            return task
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "task" by their ID
def deleteTaskDB(id_user: str, id: str):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()
        if task:
            task.deleted = True
            db.commit()
            db.refresh(task)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
        return task
