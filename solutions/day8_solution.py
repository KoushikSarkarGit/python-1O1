"""
Day 8: API Development with FastAPI
Project: Build a REST API for Task Management - SOLUTION
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


app = FastAPI(title="Task Management API", version="1.0.0")

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
    """Get all tasks with optional filtering and pagination."""
    tasks = list(tasks_db.values())
    
    if status:
        tasks = [t for t in tasks if t.status == status]
    
    tasks = tasks[skip:skip + limit]
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Get a specific task by ID."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    """Create a new task."""
    global task_id_counter
    task_id = task_id_counter
    task_id_counter += 1
    
    new_task = Task(id=task_id, **task.model_dump())
    tasks_db[task_id] = new_task
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate):
    """Update an existing task."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task = tasks_db[task_id]
    update_data = task.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(existing_task, field, value)
    
    return existing_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Delete a task."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
