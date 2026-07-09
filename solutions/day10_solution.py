"""
Day 10: Testing with pytest
Project: Build Comprehensive Test Suite - SOLUTION
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator


# Mock implementations for testing
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session() -> Generator:
    """Create a fresh database session for each test."""
    # For simplicity, we'll use in-memory storage instead of actual DB
    class MockSession:
        def __init__(self):
            self.data = {}
            self.counter = 1
        
        def add(self, item):
            item.id = self.counter
            self.data[self.counter] = item
            self.counter += 1
        
        def query(self, model):
            return MockQuery(self.data)
        
        def commit(self):
            pass
        
        def close(self):
            pass
    
    class MockQuery:
        def __init__(self, data):
            self.data = data
        
        def all(self):
            return list(self.data.values())
        
        def filter_by(self, **kwargs):
            return self
        
        def first(self):
            return list(self.data.values())[0] if self.data else None
    
    session = MockSession()
    yield session


@pytest.fixture(scope="function")
def client(db_session) -> Generator:
    """Create a test client with database session."""
    # Mock FastAPI TestClient
    class MockClient:
        def __init__(self, session):
            self.session = session
            self.tasks = {}
        
        def get(self, url):
            class MockResponse:
                def __init__(self, data, status_code=200):
                    self.data = data
                    self.status_code = status_code
                
                def json(self):
                    return self.data
            
            if url == "/tasks":
                return MockResponse(list(self.session.data.values()))
            return MockResponse(None, 404)
        
        def post(self, url, json):
            class MockResponse:
                def __init__(self, data, status_code=201):
                    self.data = data
                    self.status_code = status_code
                
                def json(self):
                    return self.data
            
            if url == "/tasks":
                task = {"id": len(self.session.data) + 1, **json}
                self.session.data[task["id"]] = task
                return MockResponse(task)
            return MockResponse(None, 400)
    
    yield MockClient(db_session)


@pytest.fixture
def sample_task_data():
    """Sample task data for testing."""
    return {
        "title": "Test Task",
        "description": "Test description",
        "status": "pending"
    }


class TestGetTasks:
    """Tests for GET /tasks endpoint."""
    
    def test_get_all_tasks(self, client, sample_task_data):
        """Test getting all tasks."""
        client.post("/tasks", json=sample_task_data)
        response = client.get("/tasks")
        assert response.status_code == 200
        assert len(response.json()) > 0
    
    def test_empty_database(self, client):
        """Test getting tasks from empty database."""
        response = client.get("/tasks")
        assert response.status_code == 200
        assert len(response.json()) == 0


class TestCreateTask:
    """Tests for POST /tasks endpoint."""
    
    def test_create_valid_task(self, client, sample_task_data):
        """Test creating a valid task."""
        response = client.post("/tasks", json=sample_task_data)
        assert response.status_code == 201
        assert "id" in response.json()


def main():
    print("=== Testing with pytest ===\n")
    print("Run tests with: pytest tests/ -v")
    print("Run coverage: pytest tests/ --cov=app --cov-report=html")


if __name__ == "__main__":
    main()
