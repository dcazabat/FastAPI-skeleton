from schemas import Task
from models import TaskDB
from cnx import SessionLocal


# Function to get all task 
def getTasks(id_user: str):
    try:
        db = SessionLocal()
        tasks_db = db.query(TaskDB).filter(TaskDB.id_user == id_user).all()
        if tasks_db:
            db.close()
            return tasks_db
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Function to get one task
def get_taskId(id_user: str, id: str):
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
def create_task(task: Task):
    try:
        db = SessionLocal()
        new_task = TaskDB(usuario_id=task.usuario_id,
                          id=task.id,
                          title=task.title,
                          summary=task.summary,
                          dataIni=task.dateIni,
                          dateEnd=task.dateEnd,
                          completed=task.completed,
                          deleted=task.deleted
                          )
        db.add(new_task)
        db.commit()
        return new_task
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to get update the "task", used in "PUT" methods
def update_task(id_user:str,  id: str, updated_task: Task):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()

        if task:
            # Actualizar los campos del usuario con los valores proporcionados en updated_user
            task.title=updated_task.title
            task.summary=updated_task.summary
            task.dataIni=updated_task.dateIni
            task.dateEnd=updated_task.dateEnd
            task.completed=updated_task.completed
            task.deleted=updated_task.deleted
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
def deleteTask(id_user: str, id: str):
    try:
        db = SessionLocal()
        task = db.query(TaskDB).filter(TaskDB.id_user == id_user, TaskDB.id == id).first()
        if task:
            db.delete(task)
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
        return task
