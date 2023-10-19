import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()
# from middlewares import salt
# Luego, al inicio de la aplicación, lee la sal desde el archivo

# stored_salt = salt.salt

# def hash_password(password: str) -> str:
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), stored_salt)
#     return hashed_password.decode('utf-8')



#Genera una nueva sal
# new_salt = bcrypt.gensalt()

# # Guarda la sal en un archivo
# with open('salt.txt', 'wb') as file:
#     file.write(new_salt)

def hash_password(password: str) -> str:
    ''' Returns an encrypted string '''
    # Codifica la contraseña en bytes antes de hashearla
    password_bytes = password.encode('utf-8')
    # Utiliza la sal almacenada
    hashed_password = bcrypt.hashpw(password_bytes, os.getenv('SECRET_KEY'))
    return hashed_password.decode('utf-8')