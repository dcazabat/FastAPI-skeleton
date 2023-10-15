from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user
from routes.tasks import task

app = FastAPI(
    openapi_tags=[{
        "Title": "REST API with FastAPI",
        "description": "CRUD users and tasks",
        "version": "0.0.1",
        "name": "CRUD",
    }]
)

# Origins admited
origins = ["*"]

# Add Middleware CORS (Cross-Origin Resource Sharing )
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(user, prefix='/users', tags=['Users'])
app.include_router(task, prefix='/tasks', tags=['Tasks'])

# General Methods

@app.get('/', tags=['Home App'])
@app.get('/home', tags=['Home App'])
def root():
    # Validate if the users and passwords are correct
    return {'message': 'Hello World'}


@app.get('/test', tags=['Home App'])
def test():
    resp = {'firtname': 'Jhon', 'lastname': 'Wick',
            'isdanger': 'Very High', 'age': 53}
    return resp
