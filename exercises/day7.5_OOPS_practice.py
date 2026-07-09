"""
Day 8: Object-Oriented Programming (OOP) in Python
Project: Build a Complete Library Management System

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Master classes, objects, constructors
- Understand instance vs class vs static methods
- Implement encapsulation with private/protected attributes
- Apply inheritance (single, multiple, multilevel, MRO)
- Use super() effectively
- Implement polymorphism (duck typing, method overriding)
- Create abstract base classes (abc module)
- Master magic/dunder methods (__str__, __repr__, __eq__, __lt__, __add__, __len__, __getitem__, __iter__, __next__, __call__, __enter__, __exit__, __hash__)
- Use @property, @setter, @deleter
- Understand composition vs inheritance
- Implement operator overloading
- Use @dataclass for boilerplate-free classes
- Implement design patterns (Singleton, Factory)
- Apply mixins for multiple inheritance
- Build custom iterators and context managers
- (Advanced) Understand descriptors and metaclasses

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a complete Library Management System that:
1. Manages books (physical, digital, audiobooks)
2. Manages members (students, faculty, premium)
3. Handles loans with due dates and fines
4. Tracks reservations and waitlists
5. Provides search and filtering
6. Supports serialization for persistence
7. Implements access control and validation
8. Provides custom iterators for collections
9. Uses context managers for loan sessions
10. Implements Singleton for the library instance

=============================================================================
TASKS TO COMPLETE:
=============================================================================

--- SECTION 1: Basics ---


2. class Member (with Encapsulation)
   - Use private attributes (__member_id, __name, __email)
   - Use protected attribute _balance
   - Provide getter/setter using @property
   - Validate email format in setter (raise ValueError if invalid)
   - Validate member_id cannot be changed after init (no setter)

3. Inheritance & Polymorphism
   - Create base class: LibraryItem (abstract)
   - Create subclasses: PhysicalBook, DigitalBook, AudioBook
   - Each subclass implements: get_loan_period(), get_late_fee_per_day()
   - Demonstrate method overriding
   - Demonstrate duck typing with a function that accepts any item with get_loan_period()

4. Multiple Inheritance & Mixins
   - Create mixins: SearchableMixin, SerializableMixin, LoggableMixin
   - SearchableMixin: provides search_by_title(), search_by_author()
   - SerializableMixin: provides to_dict(), from_dict()
   - LoggableMixin: provides log_action()
   - Apply mixins to LibraryItem

5. Abstract Base Classes
   - Create ABC: Borrowable with abstract methods: borrow(), return_item(), is_available()
   - Make LibraryItem inherit from Borrowable
   - Demonstrate that you cannot instantiate abstract class

--- SECTION 2: Magic Methods & Operator Overloading ---

6. Magic Methods on Book
   - __str__: user-friendly representation
   - __repr__: developer representation
   - __eq__: compare by ISBN
   - __lt__: compare by title (for sorting)
   - __hash__: make Book hashable (by ISBN)
   - __len__: return number of copies
   - __bool__: True if copies > 0
   - __contains__: check if author name contains substring

7. Operator Overloading
   - __add__: combine two books with same ISBN (add copies)
   - __getitem__: access book by index (return copy info)
   - __iter__: iterate over copies
   - __call__: make book callable (returns next available copy)

8. Custom Iterator Class
   - Create BookCollection class that implements __iter__ and __next__
   - Should iterate through all books
   - Support reset() method
   - Raise StopIteration when exhausted

9. Context Manager Class
   - Create LoanSession class with __enter__ and __exit__
   - On enter: mark book as borrowed, log action
   - On exit: mark book as returned (or keep if exception), log action
   - Use with statement: with LoanSession(book, member) as session:

--- SECTION 3: Properties, Data Classes, Patterns ---

10. Properties with Validation
    - Create Temperature class with celsius property
    - Add fahrenheit property (computed from celsius)
    - Use @setter with validation (cannot be below absolute zero)
    - Use @deleter to log deletion

11. @dataclass
    - Create Member dataclass with auto-generated __init__, __repr__, __eq__
    - Use field() for default values and default_factory
    - Add frozen=True to make immutable
    - Add post_init for validation

12. Singleton Pattern
    - Create Library class as Singleton
    - Use __new__ method to ensure single instance
    - Demonstrate that two instances are the same object
    - Provide thread-safe version (using lock)

13. Factory Pattern
    - Create MemberFactory class
    - Create_member(member_type) returns Student, Faculty, or PremiumMember
    - Use class method factory
    - Each member type has different borrowing limits

14. Composition vs Inheritance
    - Create Library class that HAS-A collection of books (composition)
    - Create Loan class that HAS-A book and member (composition)
    - Demonstrate why composition is preferred in some cases
    - Create a "has-a" relationship instead of "is-a"

--- SECTION 4: Advanced Topics ---

15. Descriptors (Advanced)
    - Create ValidatedString descriptor
    - Validates that string is non-empty and within length limit
    - Use __get__, __set__, __set_name__
    - Apply to Member class for name and email

16. Metaclass (Advanced)
    - Create SingletonMeta metaclass
    - Any class using this metaclass becomes Singleton automatically
    - Apply to DatabaseConnection class

17. Method Resolution Order (MRO)
    - Create diamond inheritance scenario
    - Use super() correctly in all classes
    - Print and understand __mro__
    - Demonstrate cooperative multiple inheritance

18. Complete Library System
    - Integrate all components
    - Library (Singleton) manages books and members
    - Support borrow, return, search operations
    - Generate reports
    - Serialize/deserialize data
    - Use custom exceptions

19. Custom Exceptions
    - BookNotAvailableError
    - MemberLimitExceededError
    - InvalidISBNError
    - DuplicateBookError
    - All inherit from LibraryError base class

20. Testing and Demonstration
    - Create sample data
    - Test all features
    - Demonstrate each OOP concept in action
    - Show edge cases and error handling

=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function should:
1. Create library instance (Singleton)
2. Add various books (physical, digital, audio)
3. Register members (student, faculty, premium)
4. Borrow and return books using context manager
5. Search for books using mixins
6. Serialize and deserialize data
7. Generate reports
8. Test operator overloading
9. Test custom iterators
10. Demonstrate all OOP concepts

Expected behavior:
- Only one Library instance exists
- Books can be borrowed only if available
- Members have borrowing limits based on type
- Late fees calculated correctly
- Search works across all items
- Data persists through serialization
- All magic methods work as expected

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Implement observer pattern for notifications
- Add command pattern for undo/redo operations
- Implement strategy pattern for different fine calculations
- Add unit tests for each class
- Implement plugin system for new book types
- Add GUI using tkinter
- Connect to SQLite database
- Implement REST API using Flask
- Add async support for I/O operations
- Implement visitor pattern for reports
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Iterator
from datetime import datetime, timedelta
import re
import json
import threading
import functools


# =============================================================================
# SECTION 1: BASICS - Classes, Objects, Methods
# =============================================================================
'''

1. class Book
   - Define a Book class with title, author, isbn, copies
   - Use __init__ constructor
   - Add instance method: display_info()
   - Add class variable: total_books (track all books created)
   - Add class method: from_string() (create Book from "title|author|isbn|copies")
   - Add static method: is_valid_isbn() (validate ISBN-13 format)
'''
class Book:
    """Basic Book class demonstrating class variables, class methods, static methods."""
    
    total_books = 0  # Class variable
    
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        # Done: Initialize instance variables
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        # Done: Increment total_books class variable
        Book.total_books +=1
    

    
    def display_info(self) -> str:
        """Instance method to display book info."""
        # Done: Return formatted string with book info
        return f"{self.title} by {self.author}"
    
    @classmethod
    def from_string(cls, book_str: str) -> 'Book':
        """Class method to create Book from 'title|author|isbn|copies' string."""
        # TODO: Parse string and create Book instance
        parts = book_str.split('|')
        if len(parts) == 4:
            title, author, isbn, copies = parts
            return cls(title, author, isbn, int(copies))
        elif len(parts) == 3:
            title, author, isbn = parts
            return cls(title, author, isbn)
        else:
            raise ValueError("Invalid book string format. Use 'title|author|isbn|copies'")
    
    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        """Static method to validate ISBN-13 format."""
        # TODO: Validate ISBN format (13 digits, possibly with hyphens)
        cleaned = re.sub(r'[-\s]', '', isbn)
        # Check if it's 13 digits
        if not re.match(r'^\d{13}$', cleaned):
            return False
        # Validate checksum
        total = 0
        for i, digit in enumerate(cleaned):
            d = int(digit)
            if i % 2 == 0:
                total += d
            else:
                total += d * 3
        return total % 10 == 0


class Member:
    """Member class demonstrating encapsulation with private/protected attributes."""
    
    def __init__(self, member_id: str, name: str, email: str):
        # TODO: Use private attributes __member_id, __name, __email
        # TODO: Use protected attribute _balance
        pass
    
    # TODO: Implement @property for member_id (getter only, no setter)
    
    # TODO: Implement @property and @setter for name (with validation)
    
    # TODO: Implement @property and @setter for email (with email validation)
    
    # TODO: Implement @property and @setter for balance (non-negative)


# =============================================================================
# SECTION 2: INHERITANCE & POLYMORPHISM
# =============================================================================

class LibraryItem(ABC):
    """Abstract base class for all library items."""
    
    def __init__(self, title: str, item_id: str):
        self.title = title
        self.item_id = item_id
        self._is_borrowed = False
    
    @abstractmethod
    def get_loan_period(self) -> int:
        """Return loan period in days."""
        pass
    
    @abstractmethod
    def get_late_fee_per_day(self) -> float:
        """Return late fee per day."""
        pass
    
    def is_available(self) -> bool:
        return not self._is_borrowed


class PhysicalBook(LibraryItem):
    """Physical book with specific loan period and fees."""
    
    def __init__(self, title: str, item_id: str, author: str, shelf_location: str):
        # TODO: Call super().__init__()
        # TODO: Initialize author and shelf_location
        pass
    
    def get_loan_period(self) -> int:
        # TODO: Return 14 days for physical books
        pass
    
    def get_late_fee_per_day(self) -> float:
        # TODO: Return $0.50 per day
        pass


class DigitalBook(LibraryItem):
    """Digital book with different loan period and fees."""
    
    def __init__(self, title: str, item_id: str, file_size: str, download_url: str):
        # TODO: Initialize digital book properties
        pass
    
    def get_loan_period(self) -> int:
        # TODO: Return 7 days for digital books
        pass
    
    def get_late_fee_per_day(self) -> float:
        # TODO: Return $0.00 (no late fee for digital)
        pass


class AudioBook(LibraryItem):
    """Audio book with specific properties."""
    
    def __init__(self, title: str, item_id: str, duration_minutes: int, narrator: str):
        # TODO: Initialize audio book properties
        pass
    
    def get_loan_period(self) -> int:
        # TODO: Return 21 days for audio books
        pass
    
    def get_late_fee_per_day(self) -> float:
        # TODO: Return $0.25 per day
        pass


def print_loan_info(item: LibraryItem):
    """Demonstrate duck typing - works with any LibraryItem."""
    # TODO: Print item title, loan period, and late fee
    pass


# =============================================================================
# SECTION 3: MULTIPLE INHERITANCE & MIXINS
# =============================================================================

class SearchableMixin:
    """Mixin providing search functionality."""
    
    def search_by_title(self, query: str) -> bool:
        # TODO: Return True if query is in title (case insensitive)
        pass
    
    def search_by_author(self, query: str) -> bool:
        # TODO: Return True if query is in author (case insensitive)
        # TODO: Handle case where author attribute doesn't exist
        pass


class SerializableMixin:
    """Mixin providing serialization functionality."""
    
    def to_dict(self) -> Dict[str, Any]:
        # TODO: Return dictionary representation of object
        pass
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        # TODO: Create instance from dictionary
        pass


class LoggableMixin:
    """Mixin providing logging functionality."""
    
    def log_action(self, action: str):
        # TODO: Print log message with timestamp, class name, and action
        pass


# TODO: Create EnhancedLibraryItem that inherits from LibraryItem and all mixins


# =============================================================================
# SECTION 4: MAGIC METHODS & OPERATOR OVERLOADING
# =============================================================================

class MagicBook:
    """Book class demonstrating magic methods and operator overloading."""
    
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    
    def __str__(self):
        """User-friendly string representation."""
        # TODO: Return 'MagicBook: "title" by author'
        pass
    
    def __repr__(self):
        """Developer string representation."""
        # TODO: Return 'MagicBook(title=..., author=..., isbn=..., copies=...)'
        pass
    
    def __eq__(self, other):
        """Compare by ISBN."""
        # TODO: Return True if ISBNs match
        pass
    
    def __lt__(self, other):
        """Compare by title for sorting."""
        # TODO: Return True if self.title < other.title
        pass
    
    def __hash__(self):
        """Make book hashable by ISBN."""
        # TODO: Return hash of ISBN
        pass
    
    def __len__(self):
        """Return number of copies."""
        # TODO: Return self.copies
        pass
    
    def __bool__(self):
        """True if copies > 0."""
        # TODO: Return self.copies > 0
        pass
    
    def __contains__(self, substring):
        """Check if substring is in author name."""
        # TODO: Return True if substring in author
        pass
    
    def __add__(self, other):
        """Combine two books with same ISBN."""
        # TODO: If same ISBN, return new MagicBook with combined copies
        # TODO: If different ISBN, raise ValueError
        pass
    
    def __getitem__(self, index):
        """Access copy info by index."""
        # TODO: Return copy info dict for given index
        pass
    
    def __iter__(self):
        """Iterate over copies."""
        # TODO: Yield copy info for each copy
        pass
    
    def __call__(self):
        """Make book callable - returns next available copy info."""
        # TODO: Return copy info (or None if no copies)
        pass


# =============================================================================
# SECTION 5: CUSTOM ITERATOR
# =============================================================================

class BookCollection:
    """Custom iterator class for book collections."""
    
    def __init__(self, books: List[Any] = None):
        # TODO: Initialize books list and index
        pass
    
    def __iter__(self):
        """Return iterator object (self)."""
        # TODO: Reset index and return self
        pass
    
    def __next__(self):
        """Return next book."""
        # TODO: Return next book or raise StopIteration
        pass
    
    def __len__(self):
        """Return number of books."""
        pass
    
    def add_book(self, book):
        """Add book to collection."""
        pass
    
    def reset(self):
        """Reset iterator to beginning."""
        pass


# =============================================================================
# SECTION 6: CONTEXT MANAGER
# =============================================================================

class LoanSession:
    """Context manager for book borrowing sessions."""
    
    def __init__(self, item: LibraryItem, member: 'Member'):
        # TODO: Initialize item, member, start_time
        pass
    
    def __enter__(self):
        """Called when entering 'with' block."""
        # TODO: Mark item as borrowed, log action, return self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        # TODO: If no exception, return item
        # TODO: If exception, log error but still return item
        # TODO: Log action and return False (don't suppress exception)
        pass


# =============================================================================
# SECTION 7: PROPERTIES, DATA CLASSES, PATTERNS
# =============================================================================

class Temperature:
    """Class demonstrating properties with validation."""
    
    def __init__(self, celsius: float):
        # TODO: Use private attribute _celsius
        # TODO: Use setter for validation
        pass
    
    # TODO: @property celsius (getter)
    # TODO: @celsius.setter (validate >= -273.15, raise ValueError if below)
    # TODO: @celsius.deleter (log deletion)
    
    # TODO: @property fahrenheit (computed from celsius)
    # TODO: @fahrenheit.setter (convert to celsius and set)


@dataclass
class MemberData:
    """Dataclass demonstrating auto-generated methods."""
    name: str
    email: str
    member_id: str
    age: int = 18
    borrowed_books: List[str] = field(default_factory=list)
    
    # TODO: Add __post_init__ for validation
    # TODO: Try frozen=True version


class SingletonLibrary:
    """Singleton pattern using __new__."""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        # TODO: Use lock for thread safety
        # TODO: Create instance only if _instance is None
        # TODO: Return the single instance
        pass
    
    def __init__(self, name: str = "Central Library"):
        # TODO: Initialize only once (use hasattr check)
        pass
    
    # TODO: Add methods: add_book, remove_book, find_book, list_books


class MemberFactory:
    """Factory pattern for creating different member types."""
    
    @staticmethod
    def create_member(member_type: str, name: str, email: str, member_id: str):
        """Create member based on type."""
        # TODO: Return StudentMember, FacultyMember, or PremiumMember
        # TODO: Raise ValueError for invalid type
        pass


class StudentMember(Member):
    """Student member with borrowing limit of 3."""
    borrow_limit = 3
    
    def __init__(self, name: str, email: str, member_id: str, student_id: str):
        # TODO: Call super().__init__()
        # TODO: Set student_id
        pass


class FacultyMember(Member):
    """Faculty member with borrowing limit of 10."""
    borrow_limit = 10
    
    def __init__(self, name: str, email: str, member_id: str, department: str):
        # TODO: Initialize faculty member
        pass


class PremiumMember(Member):
    """Premium member with borrowing limit of 20."""
    borrow_limit = 20
    
    def __init__(self, name: str, email: str, member_id: str, subscription_tier: str):
        # TODO: Initialize premium member
        pass


# =============================================================================
# SECTION 8: ADVANCED - DESCRIPTORS & METACLASSES
# =============================================================================

class ValidatedString:
    """Descriptor for validated string fields."""
    
    def __init__(self, min_length: int = 1, max_length: int = 100):
        # TODO: Initialize min_length, max_length, name (will be set by __set_name__)
        pass
    
    def __set_name__(self, owner, name):
        """Called when descriptor is assigned to class attribute."""
        # TODO: Store attribute name (prefix with _ for private storage)
        pass
    
    def __get__(self, obj, objtype=None):
        """Get the validated string value."""
        # TODO: Return value from obj.__dict__ or None
        pass
    
    def __set__(self, obj, value):
        """Set the validated string value."""
        # TODO: Validate: must be string, non-empty, within length limits
        # TODO: Raise ValueError if validation fails
        # TODO: Store in obj.__dict__
        pass


class ValidatedMember:
    """Member class using descriptors."""
    name = ValidatedString(min_length=2, max_length=50)
    email = ValidatedString(min_length=5, max_length=100)
    
    def __init__(self, name: str, email: str, member_id: str):
        self.name = name
        self.email = email
        self.member_id = member_id


class SingletonMeta(type):
    """Metaclass that makes any class using it a Singleton."""
    
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        # TODO: Use lock for thread safety
        # TODO: Create instance only if not in _instances
        # TODO: Return the single instance
        pass


class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection using SingletonMeta."""
    
    def __init__(self, connection_string: str = "default"):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        self.connected = True
        print(f"Connected to {self.connection_string}")


# =============================================================================
# SECTION 9: DIAMOND INHERITANCE & MRO
# =============================================================================

class A:
    def method(self):
        print("A.method")
        super().method()


class B(A):
    def method(self):
        print("B.method")
        super().method()


class C(A):
    def method(self):
        print("C.method")
        super().method()


class D(B, C):
    def method(self):
        print("D.method")
        super().method()


# =============================================================================
# SECTION 10: CUSTOM EXCEPTIONS
# =============================================================================

class LibraryError(Exception):
    """Base exception for library errors."""
    pass


class BookNotAvailableError(LibraryError):
    """Raised when book is not available for borrowing."""
    pass


class MemberLimitExceededError(LibraryError):
    """Raised when member exceeds borrowing limit."""
    pass


class InvalidISBNError(LibraryError):
    """Raised when ISBN is invalid."""
    pass


class DuplicateBookError(LibraryError):
    """Raised when adding duplicate book."""
    pass


# =============================================================================
# MAIN FUNCTION FOR TESTING
# =============================================================================

def main():
    print("=== Library Management System - OOP Practice ===\n")
    
    # SECTION 1: Test Book class
    print("1. Testing Book class (class variables, class methods, static methods):")
    # TODO: Create books, test from_string, test is_valid_isbn, test total_books
    print()
    
    # SECTION 2: Test Member class (encapsulation)
    print("2. Testing Member class (encapsulation):")
    # TODO: Create member, test getters/setters, test validation
    print()
    
    # SECTION 3: Test inheritance and polymorphism
    print("3. Testing Inheritance & Polymorphism:")
    # TODO: Create PhysicalBook, DigitalBook, AudioBook
    # TODO: Test get_loan_period(), get_late_fee_per_day()
    # TODO: Test print_loan_info() with duck typing
    print()
    
    # SECTION 4: Test mixins
    print("4. Testing Multiple Inheritance & Mixins:")
    # TODO: Create EnhancedLibraryItem
    # TODO: Test search, serialization, logging
    print()
    
    # SECTION 5: Test magic methods
    print("5. Testing Magic Methods & Operator Overloading:")
    # TODO: Create MagicBook instances
    # TODO: Test __str__, __repr__, __eq__, __lt__, __hash__
    # TODO: Test __len__, __bool__, __contains__
    # TODO: Test __add__, __getitem__, __iter__, __call__
    print()
    
    # SECTION 6: Test custom iterator
    print("6. Testing Custom Iterator:")
    # TODO: Create BookCollection
    # TODO: Add books, iterate, reset, iterate again
    print()
    
    # SECTION 7: Test context manager
    print("7. Testing Context Manager:")
    # TODO: Use 'with LoanSession(item, member) as session:'
    print()
    
    # SECTION 8: Test properties
    print("8. Testing Properties:")
    # TODO: Create Temperature, test celsius, fahrenheit, validation
    print()
    
    # SECTION 9: Test dataclass
    print("9. Testing @dataclass:")
    # TODO: Create MemberData, test auto-generated methods
    print()
    
    # SECTION 10: Test Singleton
    print("10. Testing Singleton Pattern:")
    # TODO: Create two SingletonLibrary instances, show they're same
    print()
    
    # SECTION 11: Test Factory
    print("11. Testing Factory Pattern:")
    # TODO: Create Student, Faculty, Premium members via factory
    print()
    
    # SECTION 12: Test descriptors
    print("12. Testing Descriptors:")
    # TODO: Create ValidatedMember, test validation
    print()
    
    # SECTION 13: Test metaclass
    print("13. Testing Metaclass:")
    # TODO: Create DatabaseConnection, show singleton behavior
    print()
    
    # SECTION 14: Test MRO
    print("14. Testing Method Resolution Order:")
    # TODO: Print D.__mro__
    # TODO: Call D().method() and observe order
    print()
    
    # SECTION 15: Test custom exceptions
    print("15. Testing Custom Exceptions:")
    # TODO: Try-except blocks with custom exceptions
    print()


if __name__ == "__main__":
    main()