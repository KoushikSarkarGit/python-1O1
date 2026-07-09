"""
Day 4: Context Managers & Resource Management
Project: Build a Database Connection Manager - SOLUTION
"""

import sqlite3
import tempfile
import os
import time
from contextlib import contextmanager
from typing import Optional


class DatabaseConnection:
    """Context manager for SQLite database connections."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        return False  # Don't suppress exceptions


class TransactionManager:
    """Context manager for database transactions."""
    
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor: Optional[sqlite3.Cursor] = None
    
    def __enter__(self) -> sqlite3.Cursor:
        self.cursor = self.connection.cursor()
        self.connection.execute("BEGIN")
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
        else:
            self.connection.rollback()
        if self.cursor:
            self.cursor.close()
        return False


class TemporaryFile:
    """Context manager for temporary file handling."""
    
    def __init__(self, content: str = ""):
        self.content = content
        self.file_path: Optional[str] = None
    
    def __enter__(self) -> str:
        self.file_path = tempfile.mktemp(suffix='.txt')
        with open(self.file_path, 'w') as f:
            f.write(self.content)
        return self.file_path
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_path and os.path.exists(self.file_path):
            os.unlink(self.file_path)


class Timer:
    """Context manager for timing code blocks."""
    
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time: Optional[float] = None
    
    def __enter__(self) -> 'Timer':
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"[TIMER] {self.name} took {elapsed:.4f}s")


def build_crud_system():
    """Build a complete CRUD system using all context managers."""
    with DatabaseConnection(":memory:") as conn:
        with TransactionManager(conn) as cursor:
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
            cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
            cursor.execute("INSERT INTO users VALUES (2, 'Bob')")
        
        with TransactionManager(conn) as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            print(f"  Users in database: {users}")


def main():
    print("=== Database Connection Manager ===\n")

    print("1. Testing DatabaseConnection:")
    with DatabaseConnection(":memory:") as conn:
        print(f"  Connection opened: {conn is not None}")
    print("  Connection closed automatically\n")

    print("2. Testing TransactionManager:")
    with DatabaseConnection(":memory:") as conn:
        with TransactionManager(conn) as cursor:
            cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
            cursor.execute("INSERT INTO test VALUES (1, 'Alice')")
            print("  Transaction committed")
    print()

    print("3. Testing TemporaryFile:")
    with TemporaryFile("Hello, World!") as path:
        print(f"  Temp file created: {path}")
        with open(path, 'r') as f:
            print(f"  Content: {f.read()}")
    print("  Temp file deleted automatically\n")

    print("4. Testing Timer:")
    with Timer("Sleep operation"):
        time.sleep(0.1)
    print()

    print("5. Testing complete CRUD system:")
    build_crud_system()


if __name__ == "__main__":
    main()
