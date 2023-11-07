from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import STRCNX

# Crear el motor de base de datos
engine = create_engine(STRCNX, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)