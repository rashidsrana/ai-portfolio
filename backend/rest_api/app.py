from fastapi import FastAPI, HTTPException
from models import Task
from database import tasks_db

app = FastAPI(title="Simple Task API")


@app.get("/tasks")
def get_tasks():
    return tasks_db


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(task: Task):
    new_task = task.dict()
    new_task["id"] = len(tasks_db) + 1
    tasks_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db[index].update(updated_task.dict())
            return tasks_db[index]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted = tasks_db.pop(index)
            return deleted
    raise HTTPException(status_code=404, detail="Task not found")
