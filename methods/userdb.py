from schemas import User
from models import UserDB
from cnx import SessionLocal

# Function to get all Users 
def getUsers():
    try:
        db = SessionLocal()
        users_db = db.query(UserDB).all()
        if users_db:
            db.close()
            return users_db
        return None
    except Exception as e:
        raise e
    finally:
        db.close()
# Function to get one task
def get_userId(id: str):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()
        db.close()

        return user
    except Exception as e:
        raise e
    
# Creation of "user" is used in the "POST" method
def create_user(user: UserDB):
    try:
        db = SessionLocal()
        new_user = User(
                    name=user.name,
                    firstName=user.firstName,
                    lastName=user.lastName,
                    email=user.email,
                    password=user.password,
                    deleted=user.deleted)
        db.add(new_user)
        db.commit()
        return new_user
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close_all()

# Function to get update the "User" is used in "PUT" methods
def update_user(id: str, updated_user: User):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()
        if user:
            user.nombre = updated_user.nombre
            user.edad = updated_user.edad
            user.correo = updated_user.correo
            db.commit()
            return user
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "User" by their ID
def deleteUser(id: str):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()

        if user:
            db.delete(user)
            db.commit()
        db.close()
        return user
    except Exception as e:
        raise e
    finally:
        db.close()
