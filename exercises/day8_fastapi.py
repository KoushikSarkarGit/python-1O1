"""
Day 8: API Development with FastAPI
Project: Build a REST API for Task Management

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand FastAPI basics and routing
- Learn Pydantic models for request/response validation
- Implement query parameters, path parameters, request bodies
- Create CRUD endpoints
- Add error handling and status codes
- Generate API documentation with Swagger

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a REST API for task management with:
1. CRUD operations for tasks (Create, Read, Update, Delete)
2. Validation with Pydantic models
3. Query parameters for filtering and pagination
4. Proper HTTP status codes
5. Auto-generated API documentation

=============================================================================
FASTAPI CONCEPTS:
=============================================================================
FastAPI is a modern, fast web framework for building APIs:
- Automatic type validation with Pydantic
- Automatic API documentation (Swagger UI)
- Async support
- Dependency injection

Pydantic models:
    class Task(BaseModel):
        id: int
        title: str
        completed: bool = False

Routes:
    @app.get("/tasks")
    @app.post("/tasks")
    @app.put("/tasks/{task_id}")
    @app.delete("/tasks/{task_id}")

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. Task Model (Pydantic)
   - Define TaskBase with common fields
   - Define TaskCreate for creation (no id)
   - Define TaskUpdate for updates (all optional)
   - Define Task for response (includes id)

2. GET /tasks
   - Return all tasks
   - Support query parameter for filtering completed status
   - Support skip and limit for pagination
   - Return list of tasks

3. GET /tasks/{task_id}
   - Return single task by ID
   - Return 404 if not found
   - Return task object

4. POST /tasks
   - Create new task
   - Validate request body with Pydantic
   - Generate unique ID
   - Return created task with 201 status

5. PUT /tasks/{task_id}
   - Update existing task
   - Validate request body
   - Return 404 if not found
   - Return updated task

6. DELETE /tasks/{task_id}
   - Delete task by ID
   - Return 404 if not found
   - Return 204 status on success

7. Error handling
   - Add exception handlers
   - Return proper error responses
   - Log errors

=============================================================================
TESTING YOUR CODE:
=============================================================================
Run the FastAPI server and test endpoints:
1. GET http://localhost:8000/tasks - Get all tasks
2. GET http://localhost:8000/tasks?completed=true - Filter tasks
3. GET http://localhost:8000/tasks/1 - Get specific task
4. POST http://localhost:8000/tasks - Create task
5. PUT http://localhost:8000/tasks/1 - Update task
6. DELETE http://localhost:8000/tasks/1 - Delete task

Visit http://localhost:8000/docs for Swagger UI documentation

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add authentication with JWT
- Add database integration (SQLAlchemy)
- Add unit tests with pytest
- Add CORS support
- Add rate limiting
- Add file upload for task attachments
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


app = FastAPI(title="Task Management API", version="1.0.0")


# In-memory storage (replace with database in Day 9)
tasks_db = {}
task_id_counter = 1


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = TaskStatus.PENDING


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[TaskStatus] = None


class Task(TaskBase):
    id: int
    
    class Config:
        from_attributes = True


@app.get("/")
def read_root():
    return {"message": "Task Management API", "version": "1.0.0"}


@app.get("/tasks", response_model=List[Task])
def get_tasks(
    status: Optional[TaskStatus] = Query(None, description="Filter by status"),
    skip: int = Query(0, ge=0, description="Number of tasks to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum tasks to return")
):
    """
    Get all tasks with optional filtering and pagination.
    """
    # TODO: Implement filtering and pagination
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """
    Get a specific task by ID.
    """
    # TODO: Implement get task by ID
    pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    """
    Create a new task.
    """
    # TODO: Implement task creation
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate):
    """
    Update an existing task.
    """
    # TODO: Implement task update
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """
    Delete a task.
    """
    # TODO: Implement task deletion
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
