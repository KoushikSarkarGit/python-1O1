"""
Day 8: Object-Oriented Programming (OOP) in Python
Project: Build a Complete Library Management System - SOLUTION

Exercise order:
1. Basics
2. Inheritance & Polymorphism
3. Multiple Inheritance & Mixins
4. Magic Methods & Operator Overloading
5. Custom Iterator
6. Context Manager
7. Properties, Data Classes, and Patterns
8. Advanced Topics
9. Diamond Inheritance & MRO
10. Custom Exceptions
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

class Book:
    """Basic Book class demonstrating class variables, class methods, static methods."""
    
    total_books = 0  # Class variable
    
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        Book.total_books += 1
    
    def display_info(self) -> str:
        """Instance method to display book info."""
        return f"Book: '{self.title}' by {self.author} (ISBN: {self.isbn}, Copies sold: {self.copies})"
    
    @classmethod
    def from_string(cls, book_str: str) -> 'Book':
        """Class method to create Book from 'title|author|isbn|copies' string."""
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
    """Member class demonstrating encapsulation with private/protected attributes. Also ading getter setters with property decoraters"""
    
    def __init__(self, member_id: str, name: str, email: str):
        self.__member_id = member_id  # Private
        self.__name = name            # Private
        self.__email = email          # Private
        self._balance = 0.0           # Protected
    
    @property
    def member_id(self) -> str:
        """Getter for member_id (no setter - read only)."""
        return self.__member_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self.__name = value
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, value: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email format: {value}")
        self.__email = value
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    def __str__(self):
        return f"Member(id={self.__member_id}, name={self.__name}, email={self.__email})"


# =============================================================================
# SECTION 2: INHERITANCE & POLYMORPHISM
# =============================================================================

class LibraryItem(ABC):
    """Abstract base class for all library items."""
    
    def __init__(self, title: str, item_id: str):
        self.__title  =title
        self.__item_id = item_id
        self.__is_borrowed = False
        self.__loan_period = 14
        self.__late_fee_per_day = 10.00

    @abstractmethod
    def get_loan_period(self) -> int:
        """Return loan period in days."""
        return self.__loan_period
    
    @abstractmethod
    def get_late_fee_per_day(self) -> float:
        """Return late fee per day."""
        return self.get_late_fee_per_day
    
    def is_available(self) -> bool:
        # TODO: Return if item is not borrowed
        return self.__is_borrowed
    
    def borrow(self):
        # TODO: Mark as borrowed, raise exception if already borrowed
        if self.__is_borrowed:
            raise Exception("This Book is already borrowed by someone else")
        else:
            self.__is_borrowed = True
    
    def return_item(self):

        self.__is_borrowed = False


class PhysicalBook(LibraryItem):
    """Physical book with specific loan period and fees."""
    
    def __init__(self, title: str, item_id: str, author: str, shelf_location: str):
        # TODO: Call super().__init__() and store author and shelf_location
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
        # TODO: Call super().__init__() and store file_size and download_url
        pass
    
    def get_loan_period(self) -> int:
        # TODO: Return 7 days for digital books
        pass
    
    def get_late_fee_per_day(self) -> float:
        # TODO: Return 0.00 (no late fee for digital)
        pass


class AudioBook(LibraryItem):
    """Audio book with specific properties."""
    
    def __init__(self, title: str, item_id: str, duration_minutes: int, narrator: str):
        # TODO: Call super().__init__() and store duration_minutes and narrator
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


class EnhancedLibraryItem(LibraryItem, SearchableMixin, SerializableMixin, LoggableMixin):
    """Library item with all mixins applied."""
    
    def __init__(self, title: str, item_id: str, author: str = "Unknown"):
        # TODO: Call super().__init__() and set author
        pass
    
    def get_loan_period(self) -> int:
        # TODO: Return loan period
        pass
    
    def get_late_fee_per_day(self) -> float:
        # TODO: Return late fee
        pass


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
        # TODO: Return user-friendly string representation
        pass
    
    def __repr__(self):
        # TODO: Return developer string representation
        pass
    
    def __eq__(self, other):
        # TODO: Compare by ISBN
        pass
    
    def __lt__(self, other):
        # TODO: Compare by title for sorting
        pass
    
    def __hash__(self):
        # TODO: Make book hashable by ISBN
        pass
    
    def __len__(self):
        # TODO: Return number of copies
        pass
    
    def __bool__(self):
        # TODO: True if copies > 0
        pass
    
    def __contains__(self, substring):
        # TODO: Check if substring is in author name
        pass
    
    def __add__(self, other):
        # TODO: Combine two books with same ISBN (add copies)
        pass
    
    def __getitem__(self, index):
        # TODO: Access copy info by index
        pass
    
    def __iter__(self):
        # TODO: Iterate over copies
        pass
    
    def __call__(self):
        # TODO: Make book callable - returns next available copy info
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
        # TODO: Reset index and return self
        pass
    
    def __next__(self):
        # TODO: Return next book or raise StopIteration
        pass
    
    def __len__(self):
        # TODO: Return number of books
        pass
    
    def add_book(self, book):
        # TODO: Add book to collection
        pass
    
    def reset(self):
        # TODO: Reset iterator to beginning
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
        # TODO: Mark item as borrowed, log action, return self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
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
    pass


@dataclass(frozen=True)
class FrozenMember:
    """Immutable dataclass."""
    name: str
    email: str
    member_id: str
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
        # TODO: Return StudentMember, FacultyMember, or PremiumMember
        # TODO: Raise ValueError for invalid type
        pass


class StudentMember(Member):
    """Student member with borrowing limit of 3."""
    borrow_limit = 3
    
    def __init__(self, name: str, email: str, member_id: str, student_id: str):
        # TODO: Call super().__init__() and set student_id
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
        # TODO: Store attribute name (prefix with _ for private storage)
        pass
    
    def __get__(self, obj, objtype=None):
        # TODO: Return value from obj.__dict__ or None
        pass
    
    def __set__(self, obj, value):
        # TODO: Validate: must be string, non-empty, within length limits
        # TODO: Raise ValueError if validation fails
        # TODO: Store in obj.__dict__
        pass


class ValidatedMember:
    """Member class using descriptors."""
    name = ValidatedString(min_length=2, max_length=50)
    email = ValidatedString(min_length=5, max_length=100)
    
    def __init__(self, name: str, email: str, member_id: str):
        # TODO: Set name, email, and member_id
        pass


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
        # TODO: Initialize connection_string and connected flag
        pass
    
    def connect(self):
        # TODO: Set connected to True and print message
        pass
    
    def disconnect(self):
        # TODO: Set connected to False and print message
        pass


# =============================================================================
# SECTION 9: DIAMOND INHERITANCE & MRO
# =============================================================================

class A:
    def method(self):
        # TODO: Print "A.method" and call super() if available
        pass


class B(A):
    def method(self):
        # TODO: Print "B.method" and call super()
        pass


class C(A):
    def method(self):
        # TODO: Print "C.method" and call super()
        pass


class D(B, C):
    def method(self):
        # TODO: Print "D.method" and call super() to demonstrate MRO
        pass


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
    print("=" * 60)
    print("1. Testing Book class (class variables, class methods, static methods):")
    print("=" * 60)
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
    book2 = Book("1984", "George Orwell", "9780451524935", 2)
    book3 = Book.from_string("To Kill a Mockingbird|Harper Lee|9780061120084|5")
    
    print(f"  {book1.display_info()}")
    print(f"  {book2.display_info()}")
    print(f"  {book3.display_info()}")
    print(f"  Total books created: {Book.total_books}")
    
    print(f"  ISBN '9780743273565' valid: {Book.is_valid_isbn('9780743273565')}")
    print(f"  ISBN '123' valid: {Book.is_valid_isbn('123')}")
    print()
    
    # SECTION 2: Test Member class (encapsulation)
    print("=" * 60)
    print("2. Testing Member class (encapsulation):")
    print("=" * 60)
    
    member = Member("M001", "Alice Johnson", "alice@example.com")
    print(f"  Member ID: {member.member_id}")
    print(f"  Name: {member.name}")
    print(f"  Email: {member.email}")
    print(f"  Balance: ${member.balance}")
    
    member.name = "Alice Smith"
    member.balance = 50.0
    print(f"  Updated name: {member.name}")
    print(f"  Updated balance: ${member.balance}")
    
    # Test validation
    try:
        member.email = "invalid-email"
    except ValueError as e:
        print(f"  Validation error: {e}")
    
    try:
        member.balance = -100
    except ValueError as e:
        print(f"  Validation error: {e}")
    print()
    
    # SECTION 3: Test inheritance and polymorphism
    print("=" * 60)
    print("3. Testing Inheritance & Polymorphism:")
    print("=" * 60)
    
    physical = PhysicalBook("The Hobbit", "PB001", "J.R.R. Tolkien", "A-12")
    digital = DigitalBook("Python Programming", "DB001", "15 MB", "https://example.com/download")
    audio = AudioBook("Dune", "AB001", 900, "Simon Vance")
    
    items = [physical, digital, audio]
    for item in items:
        print(f"\n  {item}")
        print_loan_info(item)
    
    # Test abstract class cannot be instantiated
    try:
        LibraryItem("Test", "TEST001")
    except TypeError as e:
        print(f"\n  Cannot instantiate abstract class: {e}")
    print()
    
    # SECTION 4: Test mixins
    print("=" * 60)
    print("4. Testing Multiple Inheritance & Mixins:")
    print("=" * 60)
    
    enhanced = EnhancedLibraryItem("The Martian", "EL001", "Andy Weir")
    print(f"  Item: {enhanced.title} by {enhanced.author}")
    print(f"  Search by title 'martian': {enhanced.search_by_title('martian')}")
    print(f"  Search by author 'weir': {enhanced.search_by_author('weir')}")
    print(f"  Serialized: {enhanced.to_dict()}")
    enhanced.log_action("Item created")
    print(f"  MRO: {[c.__name__ for c in EnhancedLibraryItem.__mro__]}")
    print()
    
    # SECTION 5: Test magic methods
    print("=" * 60)
    print("5. Testing Magic Methods & Operator Overloading:")
    print("=" * 60)
    
    mb1 = MagicBook("Python Basics", "John Doe", "9781111111111", 3)
    mb2 = MagicBook("Advanced Python", "Jane Smith", "9782222222222", 2)
    mb3 = MagicBook("Python Basics", "John Doe", "9781111111111", 1)  # Same ISBN as mb1
    
    print(f"  str: {mb1}")
    print(f"  repr: {repr(mb1)}")
    print(f"  mb1 == mb3 (same ISBN): {mb1 == mb3}")
    print(f"  mb1 < mb2 (by title): {mb1 < mb2}")
    print(f"  len(mb1): {len(mb1)}")
    print(f"  bool(mb1): {bool(mb1)}")
    print(f"  'John' in mb1: {'John' in mb1}")
    
    # Test __add__
    combined = mb1 + mb3
    print(f"  Combined copies (mb1 + mb3): {len(combined)}")
    
    # Test __getitem__
    print(f"  mb1[0]: {mb1[0]}")
    
    # Test __iter__
    print(f"  Iterating over mb1 copies:")
    for copy in mb1:
        print(f"    {copy}")
    
    # Test __call__
    print(f"  Calling mb1(): {mb1()}")
    
    # Test sorting
    books_to_sort = [mb2, mb1, mb3]
    sorted_books = sorted(set(books_to_sort))  # set uses __hash__, sorted uses __lt__
    print(f"  Sorted books: {[str(b) for b in sorted_books]}")
    print()
    
    # SECTION 6: Test custom iterator
    print("=" * 60)
    print("6. Testing Custom Iterator:")
    print("=" * 60)
    
    collection = BookCollection()
    collection.add_book(MagicBook("Book A", "Author A", "111", 1))
    collection.add_book(MagicBook("Book B", "Author B", "222", 1))
    collection.add_book(MagicBook("Book C", "Author C", "333", 1))
    
    print(f"  Collection size: {len(collection)}")
    print("  First iteration:")
    for book in collection:
        print(f"    {book}")
    
    print("  Second iteration (after reset):")
    for book in collection:
        print(f"    {book}")
    print()
    
    # SECTION 7: Test context manager
    print("=" * 60)
    print("7. Testing Context Manager:")
    print("=" * 60)
    
    test_item = PhysicalBook("Test Book", "TEST001", "Test Author", "Z-1")
    test_member = Member("M002", "Bob Wilson", "bob@example.com")
    
    print(f"  Available before: {test_item.is_available()}")
    
    with LoanSession(test_item, test_member) as session:
        print(f"  Available during loan: {test_item.is_available()}")
        print(f"  Loan started at: {session.start_time}")
    
    print(f"  Available after: {test_item.is_available()}")
    
    # Test with exception
    print("\n  Testing context manager with exception:")
    test_item2 = PhysicalBook("Another Book", "TEST002", "Another Author", "Z-2")
    try:
        with LoanSession(test_item2, test_member):
            print(f"  Available during: {test_item2.is_available()}")
            raise RuntimeError("Something went wrong!")
    except RuntimeError as e:
        print(f"  Caught exception: {e}")
    print(f"  Available after exception: {test_item2.is_available()}")
    print()
    
    # SECTION 8: Test properties
    print("=" * 60)
    print("8. Testing Properties:")
    print("=" * 60)
    
    temp = Temperature(25.0)
    print(f"  Celsius: {temp.celsius}°C")
    print(f"  Fahrenheit: {temp.fahrenheit}°F")
    
    temp.fahrenheit = 100.0
    print(f"  After setting fahrenheit=100: {temp.celsius:.2f}°C")
    
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"  Validation error: {e}")
    
    del temp.celsius
    print()
    
    # SECTION 9: Test dataclass
    print("=" * 60)
    print("9. Testing @dataclass:")
    print("=" * 60)
    
    md1 = MemberData("Charlie", "charlie@example.com", "M003", 25)
    md2 = MemberData("Charlie", "charlie@example.com", "M003", 25)
    print(f"  Member: {md1}")
    print(f"  md1 == md2: {md1 == md2}")
    print(f"  Borrowed books: {md1.borrowed_books}")
    
    frozen = FrozenMember("Dave", "dave@example.com", "M004")
    print(f"  Frozen member: {frozen}")
    
    try:
        frozen.name = "Changed"
    except AttributeError as e:
        print(f"  Cannot modify frozen: {e}")
    print()
    
    # SECTION 10: Test Singleton
    print("=" * 60)
    print("10. Testing Singleton Pattern:")
    print("=" * 60)
    
    lib1 = SingletonLibrary("My Library")
    lib2 = SingletonLibrary("Another Library")
    print(f"  lib1 is lib2: {lib1 is lib2}")
    print(f"  Library name: {lib1.name}")
    
    lib1.add_book(MagicBook("Singleton Book", "Author", "444", 1))
    print(f"  Books in lib2: {len(lib2.list_books())}")  # Same as lib1
    print()
    
    # SECTION 11: Test Factory
    print("=" * 60)
    print("11. Testing Factory Pattern:")
    print("=" * 60)
    
    student = MemberFactory.create_member('student', 'Eve', 'eve@example.com', 'M005')
    faculty = MemberFactory.create_member('faculty', 'Frank', 'frank@example.com', 'M006')
    premium = MemberFactory.create_member('premium', 'Grace', 'grace@example.com', 'M007')
    
    print(f"  {student}")
    print(f"  {faculty}")
    print(f"  {premium}")
    
    try:
        MemberFactory.create_member('invalid', 'Test', 'test@example.com', 'M008')
    except ValueError as e:
        print(f"  Error: {e}")
    print()
    
    # SECTION 12: Test descriptors
    print("=" * 60)
    print("12. Testing Descriptors:")
    print("=" * 60)
    
    vm = ValidatedMember("Henry", "henry@example.com", "M009")
    print(f"  {vm}")
    
    try:
        vm.name = "H"  # Too short
    except ValueError as e:
        print(f"  Validation error: {e}")
    
    try:
        vm.email = "x" * 200  # Too long
    except ValueError as e:
        print(f"  Validation error: {e}")
    print()
    
    # SECTION 13: Test metaclass
    print("=" * 60)
    print("13. Testing Metaclass:")
    print("=" * 60)
    
    db1 = DatabaseConnection("postgresql://localhost")
    db2 = DatabaseConnection("mysql://localhost")
    
    print(f"  db1 is db2: {db1 is db2}")
    print(f"  Connection string: {db1.connection_string}")
    db1.connect()
    print(f"  db2 connected: {db2.connected}")  # Same object
    print()
    
    # SECTION 14: Test MRO
    print("=" * 60)
    print("14. Testing Method Resolution Order:")
    print("=" * 60)
    
    print("  D.__mro__:")
    for cls in D.__mro__:
        print(f"    {cls.__name__}")
    
    print("\n  Calling D().method():")
    D().method()
    print()
    
    # SECTION 15: Test custom exceptions
    print("=" * 60)
    print("15. Testing Custom Exceptions:")
    print("=" * 60)
    
    def borrow_book(book, member):
        if not book.is_available():
            raise BookNotAvailableError(f"Book '{book.title}' is not available")
        book.borrow()
        print(f"  Borrowed: {book.title}")
    
    test_book = PhysicalBook("Exception Test", "EXC001", "Author", "X-1")
    
    # Successful borrow
    try:
        borrow_book(test_book, member)
    except LibraryError as e:
        print(f"  Error: {e}")
    
    # Try to borrow again (should fail)
    try:
        borrow_book(test_book, member)
    except BookNotAvailableError as e:
        print(f"  Expected error: {e}")
    except LibraryError as e:
        print(f"  Library error: {e}")
    
    # Test isinstance check
    try:
        raise InvalidISBNError("ISBN 123 is invalid")
    except LibraryError as e:
        print(f"  Caught LibraryError: {e}")
        print(f"  Is InvalidISBNError: {isinstance(e, InvalidISBNError)}")
    
    print("\n" + "=" * 60)
    print("=== All OOP Concepts Tested Successfully! ===")
    print("=" * 60)


if __name__ == "__main__":
    main()