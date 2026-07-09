"""
Day 9: Database Integration with SQLAlchemy
Project: Add Database to Task API - SOLUTION
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from typing import List, Optional


engine = create_engine("sqlite:///tasks.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


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
    tags = relationship("Tag", secondary=task_tag_association, back_populates="tags")
    
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', status='{self.status}')>"


def create_tables():
    """Create all tables in the database."""
    Base.metadata.create_all(engine)


def create_task(session, title: str, description: str = None, category_name: str = None) -> Task:
    """Create a new task with optional category."""
    category = None
    if category_name:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
    
    task = Task(title=title, description=description, category=category)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_task(session, task_id: int) -> Optional[Task]:
    """Get a task by ID."""
    return session.query(Task).filter_by(id=task_id).first()


def get_all_tasks(session, status: str = None, category_id: int = None) -> List[Task]:
    """Get all tasks with optional filters."""
    query = session.query(Task)
    if status:
        query = query.filter_by(status=status)
    if category_id:
        query = query.filter_by(category_id=category_id)
    return query.all()


def update_task(session, task_id: int, **kwargs) -> Optional[Task]:
    """Update a task."""
    task = get_task(session, task_id)
    if task:
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        session.commit()
        session.refresh(task)
    return task


def delete_task(session, task_id: int) -> bool:
    """Delete a task."""
    task = get_task(session, task_id)
    if task:
        session.delete(task)
        session.commit()
        return True
    return False


def add_tag_to_task(session, task_id: int, tag_name: str) -> Task:
    """Add a tag to a task."""
    task = get_task(session, task_id)
    if not task:
        return None
    
    tag = session.query(Tag).filter_by(name=tag_name).first()
    if not tag:
        tag = Tag(name=tag_name)
        session.add(tag)
    
    if tag not in task.tags:
        task.tags.append(tag)
    session.commit()
    session.refresh(task)
    return task


def get_tasks_by_category(session, category_name: str) -> List[Task]:
    """Get all tasks in a category."""
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        return category.tasks
    return []


def main():
    print("=== Database Integration with SQLAlchemy ===\n")

    create_tables()
    print("1. Tables created\n")

    session = Session()

    try:
        work_category = Category(name="Work")
        session.add(work_category)
        session.commit()
        print(f"2. Created category: {work_category}\n")

        task1 = create_task(session, "Complete project", "Finish the Python course", "Work")
        task2 = create_task(session, "Review code", "Review pull requests", "Work")
        print(f"3. Created tasks: {len([task1, task2])}\n")

        all_tasks = get_all_tasks(session)
        print(f"4. Total tasks: {len(all_tasks)}")
        for task in all_tasks:
            print(f"   {task}\n")

        add_tag_to_task(session, task1.id, "python")
        add_tag_to_task(session, task2.id, "review")
        print("5. Tags added\n")

        work_tasks = get_tasks_by_category(session, "Work")
        print(f"6. Work tasks: {len(work_tasks)}\n")

        updated = update_task(session, task1.id, status="in_progress")
        print(f"7. Updated task: {updated}\n")

        deleted = delete_task(session, task2.id)
        print(f"8. Task deleted: {deleted}\n")

    finally:
        session.close()


if __name__ == "__main__":
    main()
