from schemas.users import *
from models.users import User
from config.cnx import SessionLocal
import uuid
from middlewares.auth import hash_password

# Function to get all Users 
def getUsers():
    try:
        db = SessionLocal()
        users = db.query(User).filter(User.deleted == False).all()
        if users:
            db.close()
            return users
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Function to get one task
def getUser(id: str):
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.id == id).first()
        if user:
            db.close()
            return user
        return None
    except Exception as e:
        raise e                   
    
# Creation of "user" is used in the "POST" method
def createUser(user: CreateUserIn):
    try:
        db = SessionLocal()
        print(user.name)
        new_user = User(
                        id=str(uuid.uuid4()),
                        name=user.name,
                        firstName=user.firstName, 
                        lastName=user.lastName, 
                        email=user.email, 
                        password=hash_password(user.password)
                       )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to get update the "User" is used in "PUT" methods
def updateUser(user: UpdateUser):
    try:
        db = SessionLocal()
        updated_user = db.query(User).filter(User.id == user.id).first()
        print(updated_user)
        if updated_user:
            updated_user.firstName=user.firstName
            updated_user.lastName=user.lastName
            updated_user.email=user.email
            updated_user.password=user.password
            db.commit()
            db.refresh(updated_user)
            return updated_user
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "User" by their ID, mode logical
def deleteUser(user: DeleteUser):
    try:
        db = SessionLocal()
        delete_user = db.query(User).filter(User.id == user.id).first()
        if delete_user:
            delete_user.deleted = True
            db.commit()
            db.refresh(delete_user)
            db.close()
            return delete_user
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

def loginUser(user: LoginUser):
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.deleted == False, User.name == user.name, User.password == hash_password(user.password)).first()
        if user:
            db.close()
            return user
        return None
    except Exception as e:
        raise e
    finally:
        db.close()