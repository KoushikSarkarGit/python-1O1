"""
Day 13: Design Patterns & Architecture
Project: Refactor with Design Patterns

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand common design patterns (Singleton, Factory, Observer, Strategy)
- Learn clean architecture principles
- Implement dependency injection
- Apply SOLID principles
- Document design decisions
- Refactor existing code with patterns

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Refactor a codebase using design patterns:
1. Implement Factory pattern for object creation
2. Implement Strategy pattern for algorithms
3. Implement Observer pattern for event handling
4. Apply dependency injection
5. Create clean architecture layers
6. Document design decisions

=============================================================================
DESIGN PATTERNS CONCEPTS:
=============================================================================
Factory Pattern: Create objects without specifying exact class
    class Factory:
        def create(self, type): return ConcreteClass()

Strategy Pattern: Encapsulate algorithms
    class Strategy:
        def execute(self): pass

Observer Pattern: Subscribe to events
    class Observer:
        def update(self, event): pass

Dependency Injection: Pass dependencies instead of creating them
    def __init__(self, dependency): self.dep = dependency

SOLID Principles:
- S: Single Responsibility
- O: Open/Closed
- L: Liskov Substitution
- I: Interface Segregation
- D: Dependency Inversion

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. Factory Pattern
   - Create DatabaseFactory for different database types
   - Create LoggerFactory for different loggers
   - Use factory to create objects
   - Hide implementation details

2. Strategy Pattern
   - Create SortStrategy interface
   - Implement QuickSort, MergeSort strategies
   - Context class to use strategies
   - Switch strategies at runtime

3. Observer Pattern
   - Create Subject class with observers
   - Create Observer interface
   - Implement concrete observers
   - Notify observers on events

4. Singleton Pattern
   - Ensure only one instance exists
   - Provide global access point
   - Thread-safe implementation
   - Use for database connections, configs

5. Dependency Injection
   - Create service classes
   - Inject dependencies via constructor
   - Use dependency injection container
   - Enable testing with mocks

6. Clean Architecture
   - Separate layers (models, services, controllers)
   - Depend on abstractions, not concretions
   - Business logic independent of frameworks
   - Testable architecture

=============================================================================
TESTING YOUR CODE:
=============================================================================
Test all patterns:
1. Test Factory creates correct objects
2. Test Strategy pattern switches algorithms
3. Test Observer receives notifications
4. Test Singleton has single instance
5. Test Dependency Injection with mocks
6. Test Clean Architecture layers

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Implement Builder pattern
- Implement Decorator pattern
- Implement Adapter pattern
- Implement Command pattern
- Implement Repository pattern
- Implement Service Locator pattern
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import threading


# ============== FACTORY PATTERN ==============

class Database(ABC):
    """Abstract database interface."""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql: str):
        pass


class SQLiteDatabase(Database):
    """SQLite database implementation."""
    
    def connect(self):
        print("Connecting to SQLite database")
    
    def query(self, sql: str):
        print(f"Executing SQLite query: {sql}")


class PostgreSQLDatabase(Database):
    """PostgreSQL database implementation."""
    
    def connect(self):
        print("Connecting to PostgreSQL database")
    
    def query(self, sql: str):
        print(f"Executing PostgreSQL query: {sql}")


class DatabaseFactory:
    """Factory for creating database instances."""
    
    @staticmethod
    def create(db_type: str) -> Database:
        # TODO: Implement factory method
        pass


# ============== STRATEGY PATTERN ==============

class SortStrategy(ABC):
    """Abstract sorting strategy."""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


class QuickSort(SortStrategy):
    """Quick sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        # TODO: Implement quick sort
        pass


class MergeSort(SortStrategy):
    """Merge sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        # TODO: Implement merge sort
        pass


class Sorter:
    """Context class that uses sorting strategies."""
    
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def sort(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)


# ============== OBSERVER PATTERN ==============

class Observer(ABC):
    """Abstract observer."""
    
    @abstractmethod
    def update(self, event: str, data: Any):
        pass


class Subject:
    """Subject that notifies observers."""
    
    def __init__(self):
        self.observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        # TODO: Implement attach
        pass
    
    def detach(self, observer: Observer):
        # TODO: Implement detach
        pass
    
    def notify(self, event: str, data: Any):
        # TODO: Implement notify
        pass


class EmailNotifier(Observer):
    """Observer that sends email notifications."""
    
    def update(self, event: str, data: Any):
        print(f"Email notification: {event} - {data}")


class LogNotifier(Observer):
    """Observer that logs events."""
    
    def update(self, event: str, data: Any):
        print(f"Log: {event} - {data}")


# ============== SINGLETON PATTERN ==============

class Singleton:
    """Thread-safe singleton implementation."""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        # TODO: Implement thread-safe singleton
        pass


# ============== DEPENDENCY INJECTION ==============

class Logger:
    """Logger interface."""
    
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):
    """Console logger implementation."""
    
    def log(self, message: str):
        print(f"LOG: {message}")


class FileLogger(Logger):
    """File logger implementation."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def log(self, message: str):
        with open(self.file_path, 'a') as f:
            f.write(f"LOG: {message}\n")


class UserService:
    """Service with injected logger dependency."""
    
    def __init__(self, logger: Logger):
        self.logger = logger
    
    def create_user(self, username: str):
        self.logger.log(f"Creating user: {username}")


# ============== CLEAN ARCHITECTURE ==============

class UserRepository:
    """Repository layer for data access."""
    
    def save(self, user: Dict):
        # TODO: Implement save
        pass
    
    def find_by_id(self, user_id: int) -> Optional[Dict]:
        # TODO: Implement find
        pass


class User:
    """Domain model."""
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class UserServiceCA:
    """Service layer with business logic."""
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def create_user(self, name: str) -> User:
        user = User(id=1, name=name)
        self.repository.save({"id": user.id, "name": user.name})
        return user


def main():
    print("=== Design Patterns & Architecture ===\n")

    # Test Factory
    print("1. Testing Factory Pattern:")
    sqlite_db = DatabaseFactory.create("sqlite")
    postgres_db = DatabaseFactory.create("postgresql")
    sqlite_db.connect()
    postgres_db.connect()
    print()

    # Test Strategy
    print("2. Testing Strategy Pattern:")
    sorter = Sorter(QuickSort())
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_data = sorter.sort(data)
    print(f"  Sorted with QuickSort: {sorted_data}")
    sorter.set_strategy(MergeSort())
    print()

    # Test Observer
    print("3. Testing Observer Pattern:")
    subject = Subject()
    email_notifier = EmailNotifier()
    log_notifier = LogNotifier()
    subject.attach(email_notifier)
    subject.attach(log_notifier)
    subject.notify("user_created", {"id": 1, "name": "John"})
    print()

    # Test Singleton
    print("4. Testing Singleton Pattern:")
    s1 = Singleton()
    s2 = Singleton()
    print(f"  Same instance: {s1 is s2}")
    print()

    # Test Dependency Injection
    print("5. Testing Dependency Injection:")
    console_logger = ConsoleLogger()
    file_logger = FileLogger("app.log")
    user_service = UserService(console_logger)
    user_service.create_user("Alice")
    print()

    # Test Clean Architecture
    print("6. Testing Clean Architecture:")
    repo = UserRepository()
    service = UserServiceCA(repo)
    user = service.create_user("Bob")
    print(f"  Created user: {user.name}")


if __name__ == "__main__":
    main()
