from schemas.users import User, UpdateUser, CreateUserIn, LoginUser
from models import UserDB
from services.cnx import SessionLocal
import uuid
from middlewares.auth import hash_password

# Function to get all Users 
def getUsers():
    try:
        db = SessionLocal()
        users = db.query(UserDB).filter(UserDB.deleted == False).all()
        print('Methods')
        return users
    except Exception as e:
        raise e
    finally:
        db.close()
        print('MethodsF')

# Function to get one task
def getUserDB(id: str):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()
        db.close()
        return user
    except Exception as e:
        raise e                   
    
# Creation of "user" is used in the "POST" method
def createUserDB(user: CreateUserIn):
    try:
        db = SessionLocal()
        new_user = UserDB(
                        id=str(uuid.uuid4()),
                        name=user.name,
                        firstName=user.firstName, 
                        lastName=user.lastName, 
                        email=user.email, 
                        password=hash_password(user.password), 
                       )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close_all()

# Function to get update the "User" is used in "PUT" methods
def updateUserDB(id: str, updated_user: UpdateUser):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()
        user.firstName=updated_user.firstName
        user.lastName=updated_user.lastName
        user.email=updated_user.email
        user.password=updated_user.password
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "User" by their ID, mode logical
def deleteUserDB(id: str):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.id == id).first()
        user.deleted = True
        db.commit()
        db.refresh(user)
        db.close()
        return user
    except Exception as e:
        raise e
    finally:
        db.close()

def loginUser(user: LoginUser):
    try:
        db = SessionLocal()
        user = db.query(UserDB).filter(UserDB.deleted == False, UserDB.name == user.name, UserDB.password == hash_password(user.password)).first()
        if user:
            db.close()
            return user
        return None
    except Exception as e:
        raise e
    finally:
        db.close()