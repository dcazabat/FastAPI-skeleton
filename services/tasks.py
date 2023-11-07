from schemas.tasks import *
from models.tasks import Task
from config.cnx import SessionLocal
import uuid
from datetime import datetime

# Function to get all task 
def getTasks(id_user: str):
    try:
        db = SessionLocal()
        tasks = db.query(Task).filter(Task.id_user == id_user, Task.deleted == False).all()
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
def getTask(id_user: str, id: str):
    try:
        db = SessionLocal()
        task = db.query(Task).filter(Task.id_user == id_user, Task.id == id).first()
        if task:
            db.close()
            return task
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Creation of "Task" is used in the "POST" method
def createTask(task: CreateTaskIn):
    try:
        db = SessionLocal()
        new_task = Task(
                        id=str(uuid.uuid4()),
                        id_user=task.id_user,
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
def updateTask(task: UpdateTask):
    try:
        db = SessionLocal()
        update_task = db.query(Task).filter(Task.id_user == task.id_user, Task.id == task.id).first()

        if update_task:
            update_task.title=task.title
            update_task.summary=task.summary
            update_task.dateEnd=task.dateEnd
            update_task.completed=task.completed
            db.commit()
            db.refresh(update_task)
            db.close()
            return update_task
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def completTask(task: CompletedTask):
    try:
        db = SessionLocal()
        updated_task = db.query(Task).filter(Task.id_user == task.id_user, Task.id == task.id).first()

        if updated_task:
            updated_task.dateEnd=task.dateEnd
            updated_task.completed=task.completed
            db.commit()
            db.refresh(updated_task)
            db.close()
            return updated_task
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "task" by their ID
def deleteTask(task: DeletedTask):
    try:
        db = SessionLocal()
        delete_task = db.query(Task).filter(Task.id_user == task.id_user, Task.id == task.id).first()
        if delete_task:
            delete_task.deleted = True
            db.commit()
            db.refresh(delete_task)
            return delete_task
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
