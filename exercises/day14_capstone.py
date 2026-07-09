"""
Day 14: Capstone Project
Project: Build a Production-Ready Web Application

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Integrate ALL Week 1 and Week 2 concepts
- Build a complete production-ready application
- Implement FastAPI backend with full CRUD
- Add database integration with SQLAlchemy
- Implement authentication and authorization
- Create comprehensive test suite
- Add web scraping for data enrichment
- Implement performance optimization
- Apply design patterns
- Add Docker containerization
- Create API documentation
- Handle errors and logging

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a complete production-ready task management application that:
1. Has a FastAPI backend with full CRUD operations
2. Uses SQLAlchemy for database persistence
3. Implements JWT authentication
4. Has comprehensive pytest test suite
5. Scrapes external data for task suggestions
6. Is optimized for performance
7. Uses design patterns throughout
8. Is containerized with Docker
9. Has complete API documentation
10. Has proper error handling and logging

=============================================================================
CAPSTONE REQUIREMENTS:
=============================================================================

1. FastAPI Backend
   - Complete CRUD API for tasks
   - User management endpoints
   - Authentication endpoints
   - Proper status codes
   - Request validation with Pydantic

2. Database Layer
   - SQLAlchemy models for User, Task, Category
   - Relationship management
   - Database migrations
   - Connection pooling

3. Authentication
   - JWT token generation
   - Password hashing with bcrypt
   - Protected routes
   - Refresh tokens

4. Testing
   - Unit tests for all endpoints
   - Integration tests
   - Test fixtures
   - Coverage > 80%

5. Web Scraping
   - Scrape task suggestions from external source
   - Store in database
   - Rate limiting
   - Error handling

6. Performance
   - Caching with Redis
   - Query optimization
   - Async operations
   - Profiling

7. Design Patterns
   - Repository pattern
   - Factory pattern
   - Strategy pattern
   - Dependency injection

8. Docker
   - Dockerfile for app
   - docker-compose.yml
   - Environment variables
   - Volume mounting

9. Documentation
   - Swagger UI auto-generated
   - README with setup instructions
   - API documentation
   - Code comments

10. Error Handling
    - Global exception handlers
    - Logging configuration
    - Error responses
    - Monitoring

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. Project Structure Setup
   - Create proper directory structure
   - Separate models, services, controllers
   - Configuration management
   - Environment variables

2. Database Models
   - User model with authentication fields
   - Task model with relationships
   - Category model
   - Alembic migrations

3. Authentication System
   - Password hashing utilities
   - JWT token generation/validation
   - Login endpoint
   - Protected route decorator

4. API Endpoints
   - Auth endpoints (register, login, refresh)
   - Task CRUD endpoints
   - User endpoints
   - Category endpoints

5. Service Layer
   - TaskService with business logic
   - UserService with auth logic
   - Repository pattern for data access
   - Dependency injection

6. Web Scraping Service
   - Scrape task suggestions
   - Store in database
   - Cache results
   - Rate limiting

7. Testing Suite
   - Test all endpoints
   - Test authentication
   - Test database operations
   - Test scraping

8. Performance Optimization
   - Add caching layer
   - Optimize queries
   - Add indexes
   - Profile slow endpoints

9. Docker Setup
   - Create Dockerfile
   - Create docker-compose.yml
   - Add nginx reverse proxy
   - Configure volumes

10. Documentation
    - Complete README
    - API documentation
    - Setup guide
    - Architecture diagram

=============================================================================
TESTING YOUR CODE:
=============================================================================

1. Run all tests
   pytest tests/ -v --cov=app

2. Build Docker image
   docker build -t task-manager .

3. Run with docker-compose
   docker-compose up

4. Test API endpoints
   - Register user
   - Login and get token
   - Create task with token
   - List tasks
   - Update task
   - Delete task

5. Check Swagger UI
   http://localhost:8000/docs

=============================================================================
DELIVERABLES:
=============================================================================

1. Complete working application
2. Docker container
3. Test suite with >80% coverage
4. API documentation
5. README with setup instructions
6. Architecture documentation
7. Performance benchmarks
8. Error logs sample

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add WebSocket support for real-time updates
- Add file upload for task attachments
- Add email notifications
- Add rate limiting per user
- Add analytics dashboard
- Add internationalization (i18n)
- Add background task queue with Celery
- Add monitoring with Prometheus
- Add CI/CD pipeline
"""

# This is a capstone project - you'll build a complete application
# The structure below provides a starting point

"""
Recommended Project Structure:

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
│   ├── repositories/        # Data access
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

# Example starting point for main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
            "Category management",
            "Web scraping for suggestions",
            "Performance optimization",
            "Comprehensive testing"
        ]
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    print("=== Capstone Project: Production-Ready Task Manager ===")
    print("\nThis is your capstone project. You'll build a complete")
    print("production-ready application integrating all concepts")
    print("from Week 1 and Week 2.")
    print("\nSee the detailed requirements in the docstring above.")
    print("\nRecommended steps:")
    print("1. Set up project structure")
    print("2. Implement database models")
    print("3. Add authentication")
    print("4. Build API endpoints")
    print("5. Add service layer")
    print("6. Implement web scraping")
    print("7. Write comprehensive tests")
    print("8. Add performance optimization")
    print("9. Containerize with Docker")
    print("10. Write documentation")
    print("\nGood luck!")
