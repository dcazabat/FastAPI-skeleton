from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import create_database, database_exists, get_tables
from config import STRCNX
from models import Base

# Table Existence Check Function
def checkTable(engine, tableName):
    inspector = inspect(engine).get_table_names()
    return not tableName in inspector

# Create the database engine
engine = create_engine(STRCNX)

# First start of the Application I must know if the database is created or not and if any table is missing
if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)
# else:
#     print(checkTable(engine=engine, tableName='tasks'))
#     print(checkTable(engine=engine, tableName='users'))
#     if checkTable(engine=engine, tableName='users') or checkTable(engine=engine, tableName='tasks'):
#         Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)