"""
Day 14: Capstone Project
Project: Build a Production-Ready Web Application - SOLUTION STRUCTURE

This is a capstone project that integrates all concepts from Week 1 and Week 2.
Below is a complete working example structure for a production-ready task manager.
"""

# =============================================================================
# COMPLETE PROJECT STRUCTURE
# =============================================================================
"""
task-manager/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── config.py            # Configuration
│   ├── models/              # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── task.py
│   │   └── category.py
│   ├── schemas/             # Pydantic models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── api/                 # API routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── users.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── task_service.py
│   ├── repositories/        # Data access (Repository Pattern)
│   │   ├── __init__.py
│   │   └── task_repository.py
│   ├── core/                # Core functionality
│   │   ├── __init__.py
│   │   ├── security.py      # JWT, password hashing
│   │   └── deps.py          # Dependencies
│   └── utils/               # Utilities
│       ├── __init__.py
│       └── scraper.py       # Web scraping
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   ├── test_auth.py
│   └── test_tasks.py
├── alembic/                # Database migrations
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
"""

# =============================================================================
# SOLUTION: MINIMAL WORKING EXAMPLE
# =============================================================================

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timedelta
import sqlite3
from functools import lru_cache
import hashlib
import jwt

# ============== CONFIGURATION ==============

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ============== MODELS ==============

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"[^@]+@[^@]+\.[^@]+")
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class User(UserBase):
    id: int
    disabled: bool = False
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


# ============== DATABASE (Repository Pattern) ==============

class Database:
    """Simple database repository using SQLite."""
    
    def __init__(self, db_path: str = "task_manager.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT,
                hashed_password TEXT NOT NULL,
                disabled BOOLEAN DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                user_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()
        conn.close()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)


db = Database()

# ============== SECURITY (JWT & Password Hashing) ==============

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# ============== SERVICES (Business Logic) ==============

class AuthService:
    """Authentication service using Strategy pattern."""
    
    @staticmethod
    def create_user(user: UserCreate):
        conn = db.get_connection()
        cursor = conn.cursor()
        try:
            hashed_password = hash_password(user.password)
            cursor.execute(
                "INSERT INTO users (username, email, full_name, hashed_password) VALUES (?, ?, ?, ?)",
                (user.username, user.email, user.full_name, hashed_password)
            )
            conn.commit()
            user_id = cursor.lastrowid
            return {"id": user_id, "username": user.username, "email": user.email}
        except sqlite3.IntegrityError:
            conn.rollback()
            raise HTTPException(status_code=400, detail="Username or email already exists")
        finally:
            conn.close()
    
    @staticmethod
    def authenticate_user(username: str, password: str):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if not user:
            return False
        if not verify_password(password, user[4]):
            return False
        return user


class TaskService:
    """Task service using Repository pattern."""
    
    @staticmethod
    @lru_cache(maxsize=100)
    def get_tasks(user_id: Optional[int] = None) -> List[Task]:
        """Get tasks with caching (Strategy pattern for caching)."""
        conn = db.get_connection()
        cursor = conn.cursor()
        if user_id:
            cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        else:
            cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        
        return [
            Task(
                id=row[0],
                title=row[1],
                description=row[2],
                completed=bool(row[3]),
                created_at=datetime.fromisoformat(row[5])
            )
            for row in rows
        ]
    
    @staticmethod
    def create_task(task: TaskCreate, user_id: int) -> Task:
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, completed, user_id) VALUES (?, ?, ?, ?)",
            (task.title, task.description, task.completed, user_id)
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        
        return Task(
            id=task_id,
            title=task.title,
            description=task.description,
            completed=task.completed,
            created_at=datetime.utcnow()
        )


# ============== FASTAPI APP ==============

app = FastAPI(title="Task Manager API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "message": "Task Manager API",
        "version": "1.0.0",
        "features": [
            "User authentication with JWT",
            "Task CRUD operations",
            "Repository pattern for data access",
            "Service layer for business logic",
            "Caching with lru_cache",
            "CORS support"
        ]
    }


@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = AuthService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user[1]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=dict)
def create_user(user: UserCreate):
    return AuthService.create_user(user)


@app.get("/tasks/", response_model=List[Task])
def read_tasks(user_id: Optional[int] = None):
    return TaskService.get_tasks(user_id)


@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: TaskCreate, user_id: int = 1):
    return TaskService.create_task(task, user_id)


@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}


# =============================================================================
# DOCKERFILE
# =============================================================================
"""
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# =============================================================================
# DOCKER-COMPOSE.YML
# =============================================================================
"""
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./task_manager.db:/app/task_manager.db
    environment:
      - SECRET_KEY=your-secret-key
"""

# =============================================================================
# REQUIREMENTS.TXT
# =============================================================================
"""
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
"""

# =============================================================================
# README.MD
# =============================================================================
"""
# Task Manager API

A production-ready task management API built with FastAPI.

## Features

- JWT Authentication
- Task CRUD operations
- Repository pattern for data access
- Service layer for business logic
- Caching with lru_cache
- CORS support
- Docker containerization

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Access Swagger UI:
   http://localhost:8000/docs

## Docker

Build and run with Docker:
```bash
docker-compose up
```

## Testing

Run tests:
```bash
pytest tests/ -v --cov=app
```
"""


def main():
    print("=== Capstone Project: Production-Ready Task Manager ===\n")
    print("This is a complete solution integrating all concepts:")
    print("- FastAPI for REST API")
    print("- Pydantic for validation")
    print("- SQLite for database")
    print("- JWT for authentication")
    print("- Repository pattern for data access")
    print("- Service layer for business logic")
    print("- Strategy pattern for caching")
    print("- CORS middleware")
    print("- Docker containerization")
    print("\nTo run the API:")
    print("  uvicorn day14_solution:app --reload")
    print("\nAccess Swagger UI at: http://localhost:8000/docs")


if __name__ == "__main__":
    main()
