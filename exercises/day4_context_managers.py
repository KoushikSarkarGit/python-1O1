"""
Day 4: Context Managers & Resource Management
Project: Build a Database Connection Manager

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand the context manager protocol (__enter__, __exit__)
- Learn how to use 'with' statement for automatic resource cleanup
- Implement custom context managers
- Use contextlib module for simpler context managers
- Handle exceptions in context managers
- Build practical resource management systems

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a database connection manager that automatically handles:
1. Opening and closing database connections
2. Transaction management (commit/rollback)
3. Temporary file handling with automatic cleanup
4. Code block timing with automatic reporting
5. Complete CRUD operations using context managers

=============================================================================
CONTEXT MANAGER CONCEPTS:
=============================================================================
Context managers enable automatic resource cleanup using the 'with' statement.
They implement two methods:
- __enter__(self): Called when entering the 'with' block
- __exit__(self, exc_type, exc_val, exc_tb): Called when exiting

Basic usage:
    with MyContextManager() as resource:
        # Use resource
    # Automatic cleanup happens here

The contextlib module provides decorators for simple context managers:
    @contextmanager
    def my_context():
        # Setup
        yield resource
        # Cleanup

=============================================================================
TASKS TO COMPLETE:
=============================================================================



=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests all context managers:
1. DatabaseConnection - Opens and closes connection
2. TransactionManager - Commits successful operations, rolls back on error
3. TemporaryFile - Creates file, writes to it, auto-deletes
4. Timer - Measures execution time of code blocks
5. CRUD System - Complete database operations

Expected behavior:
- Connections are automatically closed
- Transactions commit on success, rollback on failure
- Temporary files are deleted after use
- Timer reports execution time
- CRUD operations work with automatic resource management

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Create a context manager for HTTP sessions
- Implement a context manager for thread locks
- Create a context manager that changes directory temporarily
- Build a context manager for logging indentation
- Implement a context manager for retrying operations
- Create a context manager for measuring memory usage
"""
 
import sqlite3
import tempfile
import os
import time
from contextlib import contextmanager
from typing import Optional

'''
1. DatabaseConnection (Context Manager Class)
   - Implement __enter__ to open SQLite connection
   - Implement __exit__ to close connection
   - Handle exceptions in __exit__ (return True to suppress, False to propagate)
   - Store connection as self.connection
   - Return connection in __enter__ for use in 'with' block

'''
class DatabaseConnection:
    """Context manager for SQLite database connections."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self) -> sqlite3.Connection:
        # Done:  Open database connection and return it
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Done: Close connection, handle exceptions
        if self.connection:
            self.connection.close()

        return False






'''
2. TransactionManager (Context Manager Class)
   - Accept a database connection in __init__
   - Begin transaction in __enter__
   - Commit in __exit__ if no exception occurred
   - Rollback in __exit__ if exception occurred
   - Return cursor in __enter__ for executing queries


'''

class TransactionManager:
    """Context manager for database transactions."""
    
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor: Optional[sqlite3.Cursor] = None
    
    def __enter__(self) -> sqlite3.Cursor:
        # TODO: Begin transaction, return cursor
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Commit or rollback based on exception
        pass



'''
3. TemporaryFile (Context Manager Class)
   - Create a temporary file in __enter__
   - Write initial content if provided
   - Delete the file in __exit__
   - Return file path in __enter__
   - Use tempfile module for temporary file creation

'''


class TemporaryFile:
    """Context manager for temporary file handling."""
    
    def __init__(self, content: str = ""):
        self.content = content
        self.file_path: Optional[str] = None
    
    def __enter__(self) -> str:
        # TODO: Create temp file, write content, return path
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Delete the temporary file
        pass


'''
4. Timer (Context Manager Class)
   - Record start time in __enter__
   - Calculate elapsed time in __exit__
   - Print elapsed time in __exit__
   - Return self in __enter__ (optional)
   - Use time.time() for timing


'''

class Timer:
    """Context manager for timing code blocks."""
    
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time: Optional[float] = None
    
    def __enter__(self) -> 'Timer':
        # TODO: Record start time, return self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Calculate and print elapsed time
        pass


'''
5. build_crud_system()
   - Use all context managers together
   - Create a table using TransactionManager
   - Insert records using TransactionManager
   - Query records using TransactionManager
   - Demonstrate automatic cleanup
'''

def build_crud_system():
    """Build a complete CRUD system using all context managers."""
    # TODO: Implement using all context managers
    pass


def main():
    print("=== Database Connection Manager ===\n")

    # Test DatabaseConnection
    print("1. Testing DatabaseConnection:")
    with DatabaseConnection(":memory:") as conn:
        print(f"  Connection opened: {conn is not None}")
    print("  Connection closed automatically\n")

    # Test TransactionManager
    print("2. Testing TransactionManager:")
    with DatabaseConnection(":memory:") as conn:
        with TransactionManager(conn) as cursor:
            cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
            cursor.execute("INSERT INTO test VALUES (1, 'Alice')")
            print("  Transaction committed")
    print()

    # Test TemporaryFile
    print("3. Testing TemporaryFile:")
    with TemporaryFile("Hello, World!") as path:
        print(f"  Temp file created: {path}")
        with open(path, 'r') as f:
            print(f"  Content: {f.read()}")
    print("  Temp file deleted automatically\n")

    # Test Timer
    print("4. Testing Timer:")
    with Timer("Sleep operation"):
        time.sleep(0.1)
    print()

    # Test CRUD system
    print("5. Testing complete CRUD system:")
    build_crud_system()


if __name__ == "__main__":
    main()
