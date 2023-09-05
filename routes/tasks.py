from fastapi import APIRouter
from fastapi import HTTPException
from schemas import Task, UpdateTask, CreateTask, CompletedTask
from methods.taskdb import getTasks, getTaskDB, createTaskDB, updateTaskDB, deleteTaskDB, completTaskDB

task = APIRouter()

# Method for Task
@task.get('/{id_user}', response_model=list[Task], tags=['Tasks'])
async def get_all_task(id_user: str):
    # Send all users
    try:
        tasks = getTasks(id_user=id_user)
        if tasks:
            return tasks
        raise HTTPException(status_code=404, detail=f'Tasks: not found for User ({id_user})')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting tasks: {e}")

@task.get('/{id_user}/{id}',response_model=Task , tags=['Tasks'])
async def get_task(id_user: str, id: str):
    # Check if task exists
    try:
        task = getTaskDB(id_user=id_user, id=id)
        if task:
            return task
        raise HTTPException(status_code=404, detail=f'Task: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting task {id}: {e}")

@task.post('/{id_user}',response_model=CreateTask , tags=['Tasks'])
async def create_task(id_user: str, task: CreateTask):
    try:
        new_task = createTaskDB(id_user=id_user, task=task)
        return new_task
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: Task creation failed: {e}")

@task.put('/{id_user}/{id}',response_model=UpdateTask , tags=['Tasks'])
async def update_task(id_user: str, id: str, task: UpdateTask):
    try:
        updatedTask = updateTaskDB(id_user=id_user, id=id, task=task)
        if updatedTask:
            return updatedTask
        raise HTTPException(status_code=404, detail=f'Task: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Task ID: {id}, Error {e}")

@task.patch('/{id_user}/{id}',response_model=CompletedTask , tags=['Tasks'])
async def completed_task(id_user: str, id: str, task: CompletedTask):
    try:
        completedTask = completTaskDB(id_user=id_user, id=id, task=task)
        if completedTask:
            return completedTask
        raise HTTPException(status_code=404, detail=f'Task: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Completed Failed for Task ID: {id}, Error {e}")

@task.delete('/{id_user}/{id}',response_model=Task , tags=['Tasks'])
async def delete_task(id_user: str, id: str):
    try:
        deletedTask = deleteTaskDB(id_user=id_user, id=id)
        if deletedTask:
            return deletedTask
        raise HTTPException(status_code=404, detail=f'Task: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Task ID: {id}, Error {e}")