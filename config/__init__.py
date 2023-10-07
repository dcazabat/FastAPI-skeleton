import os
from dotenv import load_dotenv

load_dotenv()

# The .env file must be created with the .env.example format
# With SQLite
# STRCNX='sqlite:///mydb.db'

## ---------------------------------------------------------------------------

# With MySQL, we must have installed pymysql

# Basic
# HOST='SU_HOST' 
# USER='SU_USER'
# PWDS='SU_PASSWORD'
# DBA='SU_BASE_DE_DATOS'
# PORT='SU_PUERTO'

# Example:
HOST=os.getenv('HOST')
USERDB=os.getenv('USERDB')
PWDS=os.getenv('PWDS')
DBA=os.getenv('DBA')
PORT=os.getenv('PORT')
STRCNX=f'mysql+pymysql://{USERDB}:{PWDS}@{HOST}:{PORT}/{DBA}'
print(STRCNX)
SQLALCHEMY_DATABASE_URI=STRCNX