from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from config.cnx import engine
from routes.routeapp import default
from routes.users import user
from routes.tasks import task

app = FastAPI(
    openapi_tags=[{
        "Title": "REST API with FastAPI",
        "description": "CRUD users and tasks",
        "version": "1.1.0",
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
app.include_router(default, prefix='', tags=['App Default'])
app.include_router(user, prefix='/users', tags=['Users'])
app.include_router(task, prefix='/tasks', tags=['Tasks'])

Base.metadata.create_all(bind=engine)