import os
from pathlib import Path

# Load environment variables from file .env
from dotenv import load_dotenv
load_dotenv()

# I configure the database engine and the connection string

# The .env file must be created with the .env.example format
# With SQLite
# STRCNX='sqlite:///mydb.db'

ENGINE=os.getenv('ENGINE')
HOST= os.getenv('HOST')
USERDB= os.getenv('USERDB')
PWDS= os.getenv('PWDS')
DBA= os.getenv('DBA')
PORT= os.getenv('PORT')

STRCNX2=f'{ENGINE}://{USERDB}:{PWDS}@{HOST}:{PORT}/{DBA}'
print(STRCNX2)
SQLALCHEMY_DATABASE_URI=STRCNX