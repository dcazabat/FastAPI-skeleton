# I configure the database engine and the connection string

# With SQLite
STRCNX='sqlite:///mydb.db'

## ---------------------------------------------------------------------------

# With MySQL, we must have installed pymysql

# Basic
# HOST='SU_HOST' 
# USER='SU_USER'
# PWDS='SU_PASSWORD'
# DBA='SU_BASE_DE_DATOS'
# PORT='SU_PUERTO'

# Example:
# HOST='192.168.0.10' 
# USER='root'
# PWDS='Dany5170#'
# DBA='sampledbpy'
# PORT='3306'
# STRCNX=f'mysql+pymysql://{USER}:{PWDS}@{HOST}:{PORT}/{DBA}'
SQLALCHEMY_DATABASE_URI=STRCNX