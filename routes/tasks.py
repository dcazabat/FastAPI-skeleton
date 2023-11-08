from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.tasks import *
from services.tasks import *
from typing import List

task = APIRouter()

# Method for Task
@task.get('/{id_user}', response_model=List[TaskOut], status_code=200)
async def get_all_task(id_user: str):
    # Send all users
    try:
        tasks = getTasks(id_user=id_user)
        if tasks:
            return tasks
        return JSONResponse(status_code=404, content=f'Tasks: not found for User ({id_user})')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting tasks: {e}")

@task.get('/{id_user}/{id}',response_model=TaskOut, status_code=200)
async def get_task(id_user: str, id: str):
    # Check if task exists
    try:
        task = getTask(id_user=id_user, id=id)
        if task:
            return task
        return JSONResponse(status_code=404, content=f'Task: {id} not found for User ({id_user})')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting task {id}: {e}")

@task.post('',response_model=TaskOut, status_code=200)
async def create_task(task: CreateTaskIn):
    try:
        new_task = createTask(task=task)
        if new_task:
            return new_task
        return JSONResponse(status_code=404, content=f'Task: not Create for User ({task.id_user})')
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: Task creation failed: {e}")

@task.put('',response_model=TaskOut, status_code=200)
async def update_task(task: UpdateTask):
    try:
        updatedTask = updateTask(task=task)
        if updatedTask:
            return updatedTask
        return JSONResponse(status_code=404, content=f'Task: {id} not Update for User ({task.id_user})')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Task ID: {id}, Error {e}")

@task.patch('',response_model=TaskOut, status_code=200)
async def completed_task(task: CompletedTask):
    try:
        completedTask = completTask(task=task)
        if completedTask:
            return completedTask
        return JSONResponse(status_code=404, content=f'Task: {id} not Mark of Completed for User ({task.id_user})')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Completed Failed for Task ID: {id}, Error {e}")

@task.delete('',response_model=TaskOut, status_code=200)
async def delete_task(task: DeletedTask):
    try:
        deletedTask = deleteTask(task=task)
        if deletedTask:
            return deletedTask
        return JSONResponse(status_code=404, content=f'Task: {id} not Delete for User ({task.id_user})')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Task ID: {id}, Error {e}")