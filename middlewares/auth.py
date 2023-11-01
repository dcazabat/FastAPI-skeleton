import bcrypt
import os
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

from dotenv import load_dotenv


load_dotenv()

def hash_password(password: str) -> str:
    ''' Returns an encrypted string '''
    # Codifica la contraseña en bytes antes de hashearla
    password_bytes = password.encode('utf-8')
    # Utiliza la sal almacenada
    hashed_password = bcrypt.hashpw(password_bytes, os.getenv('SECRET_KEY'))
    return hashed_password.decode('utf-8')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt


### REVISAR 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Middleware para verificar el token JWT
async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        # Aquí podrías realizar validaciones adicionales si lo necesitas
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")