"""
Day 13: Design Patterns & Architecture
Project: Refactor with Design Patterns - SOLUTION
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
        if db_type == "sqlite":
            return SQLiteDatabase()
        elif db_type == "postgresql":
            return PostgreSQLDatabase()
        else:
            raise ValueError(f"Unknown database type: {db_type}")


# ============== STRATEGY PATTERN ==============

class SortStrategy(ABC):
    """Abstract sorting strategy."""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


class QuickSort(SortStrategy):
    """Quick sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class MergeSort(SortStrategy):
    """Merge sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


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
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, event: str, data: Any):
        for observer in self.observers:
            observer.update(event, data)


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
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


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
    
    def __init__(self):
        self.data = {}
    
    def save(self, user: Dict):
        self.data[user['id']] = user
    
    def find_by_id(self, user_id: int) -> Optional[Dict]:
        return self.data.get(user_id)


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
        user_id = len(self.repository.data) + 1
        user = User(id=user_id, name=name)
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
    print(f"   Sorted with QuickSort: {sorted_data}")
    sorter.set_strategy(MergeSort())
    sorted_data = sorter.sort(data)
    print(f"   Sorted with MergeSort: {sorted_data}\n")

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
    print(f"   Same instance: {s1 is s2}")
    print()

    # Test Dependency Injection
    print("5. Testing Dependency Injection:")
    console_logger = ConsoleLogger()
    user_service = UserService(console_logger)
    user_service.create_user("Alice")
    print()

    # Test Clean Architecture
    print("6. Testing Clean Architecture:")
    repo = UserRepository()
    service = UserServiceCA(repo)
    user = service.create_user("Bob")
    print(f"   Created user: {user.name}")


if __name__ == "__main__":
    main()
