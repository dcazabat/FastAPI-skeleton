from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import create_database, database_exists, get_tables
from config import STRCNX
from models import Base

# Function Test Table Exist
def checkTable(engine, tableName):
    inspector = inspect(engine).get_table_names()
    return not tableName in inspector

# Crear el motor de base de datos
engine = create_engine(STRCNX)

# Pimer inicio de la Aplicacion debo saber si la base de datos esta creada o no
if not database_exists(engine.url):
    create_database(engine.url)
else:
    if checkTable(engine=engine, tableName='users') and checkTable(engine=engine, tableName='tasks'):
        Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)