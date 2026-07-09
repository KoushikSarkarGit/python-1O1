"""
Day 9: Database Integration with SQLAlchemy
Project: Add Database to Task API

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand SQLAlchemy ORM basics
- Learn database models and relationships
- Implement CRUD operations with ORM
- Handle database transactions
- Add relationship management
- Use database migrations

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Extend the Task API from Day 8 with database persistence:
1. Design database schema for tasks
2. Create SQLAlchemy models
3. Implement database CRUD operations
4. Add relationship management (categories, tags)
5. Handle database transactions
6. Add database migrations

=============================================================================
SQLALCHEMY CONCEPTS:
=============================================================================
SQLAlchemy is an ORM (Object-Relational Mapping) library:
- Maps Python classes to database tables
- Provides a high-level abstraction over SQL
- Supports multiple database backends

Models:
    class Task(Base):
        __tablename__ = "tasks"
        id = Column(Integer, primary_key=True)
        title = Column(String)

CRUD operations:
    session.add(task)  # Create
    session.query(Task).all()  # Read
    session.query(Task).filter_by(id=1).update(...)  # Update
    session.delete(task)  # Delete

Relationships:
    tasks = relationship("Task", back_populates="category")

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. Database Setup
   - Create engine with SQLite
   - Create declarative base
   - Create session factory

2. Task Model
   - Define Task class inheriting from Base
   - Add columns: id, title, description, status, created_at
   - Add __repr__ for debugging

3. Category Model
   - Define Category class
   - Add columns: id, name
   - Add relationship to tasks

4. Tag Model
   - Define Tag class
   - Add columns: id, name
   - Add many-to-many relationship with tasks

5. CRUD Operations
   - create_task: Insert new task
   - get_task: Query by ID
   - get_all_tasks: Query all with filters
   - update_task: Update existing task
   - delete_task: Delete task

6. Relationship Operations
   - Add category to task
   - Add tags to task
   - Query tasks by category
   - Query tasks by tag

7. Transaction Management
   - Use context manager for sessions
   - Commit on success
   - Rollback on error

=============================================================================
TESTING YOUR CODE:
=============================================================================
Test all CRUD operations:
1. Create database and tables
2. Create tasks with categories and tags
3. Query tasks with filters
4. Update task properties
5. Delete tasks
6. Test relationship queries

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add Alembic for database migrations
- Add indexes for performance
- Implement soft delete
- Add full-text search
- Add database connection pooling
- Implement caching with Redis
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from typing import List, Optional


# Database setup
engine = create_engine("sqlite:///tasks.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Many-to-many relationship table for tasks and tags
task_tag_association = Table(
    'task_tags',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Category(Base):
    """Category model for task categorization."""
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    tasks = relationship("Task", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


class Tag(Base):
    """Tag model for task labeling."""
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    tasks = relationship("Task", secondary=task_tag_association, back_populates="tags")
    
    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"


class Task(Base):
    """Task model for task management."""
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    status = Column(String(20), default="pending")
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship("Category", back_populates="tasks")
    tags = relationship("Tag", secondary=task_tag_association, back_populates="tasks")
    
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', status='{self.status}')>"


def create_tables():
    """Create all tables in the database."""
    # TODO: Create all tables
    pass


def create_task(session, title: str, description: str = None, category_name: str = None) -> Task:
    """Create a new task with optional category."""
    # TODO: Implement task creation
    pass


def get_task(session, task_id: int) -> Optional[Task]:
    """Get a task by ID."""
    # TODO: Implement get task
    pass


def get_all_tasks(session, status: str = None, category_id: int = None) -> List[Task]:
    """Get all tasks with optional filters."""
    # TODO: Implement get all tasks with filters
    pass


def update_task(session, task_id: int, **kwargs) -> Optional[Task]:
    """Update a task."""
    # TODO: Implement task update
    pass


def delete_task(session, task_id: int) -> bool:
    """Delete a task."""
    # TODO: Implement task deletion
    pass


def add_tag_to_task(session, task_id: int, tag_name: str) -> Task:
    """Add a tag to a task."""
    # TODO: Implement adding tag to task
    pass


def get_tasks_by_category(session, category_name: str) -> List[Task]:
    """Get all tasks in a category."""
    # TODO: Implement query by category
    pass


def main():
    print("=== Database Integration with SQLAlchemy ===\n")

    # Create tables
    print("1. Creating tables:")
    create_tables()
    print("  Tables created\n")

    # Create session
    session = Session()

    try:
        # Create category
        print("2. Creating category:")
        work_category = Category(name="Work")
        session.add(work_category)
        session.commit()
        print(f"  Created category: {work_category}\n")

        # Create tasks
        print("3. Creating tasks:")
        task1 = create_task(session, "Complete project", "Finish the Python course", "Work")
        task2 = create_task(session, "Review code", "Review pull requests", "Work")
        print(f"  Created tasks: {len([task1, task2])}\n")

        # Query tasks
        print("4. Querying tasks:")
        all_tasks = get_all_tasks(session)
        print(f"  Total tasks: {len(all_tasks)}")
        for task in all_tasks:
            print(f"    {task}\n")

        # Add tags
        print("5. Adding tags:")
        add_tag_to_task(session, task1.id, "python")
        add_tag_to_task(session, task2.id, "review")
        print("  Tags added\n")

        # Query by category
        print("6. Querying by category:")
        work_tasks = get_tasks_by_category(session, "Work")
        print(f"  Work tasks: {len(work_tasks)}\n")

        # Update task
        print("7. Updating task:")
        updated = update_task(session, task1.id, status="in_progress")
        print(f"  Updated task: {updated}\n")

        # Delete task
        print("8. Deleting task:")
        deleted = delete_task(session, task2.id)
        print(f"  Task deleted: {deleted}\n")

    finally:
        session.close()


if __name__ == "__main__":
    main()
