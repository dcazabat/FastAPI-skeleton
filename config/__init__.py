import os
from dotenv import load_dotenv

# Load environment variables from file .env
load_dotenv()

# I configure the database engine and the connection string

# With SQLite
# STRCNX='sqlite:///mydb.db'

ENGINE=os.getenv('ENGINE')
HOST= os.getenv('HOST')
USERDB= os.getenv('USERDB')
PWDS= os.getenv('PWDS')
DBA= os.getenv('DBA')
PORT= os.getenv('PORT')

STRCNX=f'{ENGINE}://{USERDB}:{PWDS}@{HOST}:{PORT}/{DBA}'
SQLALCHEMY_DATABASE_URI=STRCNX