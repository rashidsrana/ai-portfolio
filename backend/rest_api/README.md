# Simple Python REST API (FastAPI)

This is a lightweight REST API built with FastAPI to demonstrate Python backend development skills.  
It includes CRUD operations for a simple "Task" resource using in-memory storage (loads tasks_db array into memory)

## Features
- Create tasks
- Retrieve all tasks
- Retrieve a single task
- Update tasks
- Delete tasks
- Clean, modern FastAPI structure

## Tech Stack
- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

## How to Run

Install dependencies:


## Run the server
 c:\python314\python.exe -m uvicorn app:app --reload


## The Rest API test (Loca env) (Similar like Swagger)
It can be tested in browser, such as http://127.0.0.1:8000/docs
GET /tasks
Get Tasks
POST /tasks
Create Task
GET /tasks/{task_id}
Get Task
PUT /tasks/{task_id}
Update Task
DELETE /tasks/{task_id}
Delete Task

## Sample payload
{
  "title": "Buy groceries",
  "description": "Milk, eggs",
  "completed": false
}

## In memory the Posted payload:
[
  {"id": 1, "title": "Buy groceries", "description": "Milk, eggs", "completed": false}
]
