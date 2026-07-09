"""
Day 0: Python Core Concepts Revision
Project: Comprehensive Basics Refresher - SOLUTION
"""

# =============================================================================
# EXERCISE 1: DATA TYPES
# =============================================================================

def exercise_1_data_types():
    """Practice with data types and operations."""
    print("=== Exercise 1: Data Types ===")
    
    # Create variables of different types
    age = 25  # int
    price = 99.99  # float
    name = "Alice"  # str
    is_active = True  # bool
    
    # Type conversions
    age_str = str(age)
    name_age = name + " is " + age_str
    price_str = "99.99"
    price_float = float(price_str)
    discounted_price = price_float * 0.9
    
    # String methods
    text = "  Hello World  "
    stripped = text.strip()
    upper = stripped.upper()
    lower = stripped.lower()
    words = stripped.split()
    joined = " ".join(words)
    
    # String formatting with f-strings
    formatted = f"Name: {name}, Age: {age}, Price: ${price:.2f}"
    
    print(f"Name: {name}, Age: {age}, Price: ${price:.2f}")
    print(f"Formatted: {formatted}")
    print(f"Processed text: '{stripped}' -> '{upper}' -> '{lower}'")
    print()


# =============================================================================
# EXERCISE 2: LISTS & TUPLES
# =============================================================================

def exercise_2_lists():
    """Practice with lists and tuples."""
    print("=== Exercise 2: Lists & Tuples ===")
    
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # List operations
    numbers.append(6)  # Add 6 to the end
    numbers.insert(0, 0)  # Insert 0 at the beginning
    numbers.remove(3)  # Remove the number 3
    numbers.reverse()  # Reverse the list
    
    # List comprehension
    squares = [x**2 for x in range(1, 11)]
    
    # Create a tuple
    coordinates = (10, 20, 30)
    
    # Tuple unpacking
    x, y, z = coordinates
    
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    print(f"Coordinates: {coordinates}")
    print(f"Unpacked: x={x}, y={y}, z={z}")
    print()


# =============================================================================
# EXERCISE 3: DICTIONARIES & SETS
# =============================================================================

def exercise_3_dictionaries():
    """Practice with dictionaries and sets."""
    print("=== Exercise 3: Dictionaries & Sets ===")
    
    # Create a dictionary for a person
    person = {"name": "Alice", "age": 25, "city": "NYC"}
    
    # Dictionary operations
    person["email"] = "alice@example.com"  # Add email
    person["age"] = 26  # Update age
    city = person.get("city", "Unknown")  # Get city with default
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    
    # Dictionary comprehension
    doubled = {num: num*2 for num in range(5)}
    
    # Create a set
    unique_numbers = {1, 2, 3, 2, 1, 4}
    
    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    union = set1 | set2
    intersection = set1 & set2
    
    print(f"Person: {person}")
    print(f"Doubled: {doubled}")
    print(f"Unique numbers: {unique_numbers}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print()


# =============================================================================
# EXERCISE 4: CONTROL FLOW
# =============================================================================

def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero" 


def exercise_4_control_flow():
    """Practice with control flow."""
    print("=== Exercise 4: Control Flow ===")
    
    # Test check_number function
    print(f"5 is: {check_number(5)}")
    print(f"-3 is: {check_number(-3)}")
    print(f"0 is: {check_number(0)}")
    
    # For loop - print even numbers 1-20
    print("Even numbers 1-20:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(f"  {i}", end=" ")
    print()
    
    # While loop example
    print("\nWhile loop example (sum until 0):")
    total = 0
    numbers = [1, 2, 3, 0, 4, 5]
    for num in numbers:
        if num == 0:
            break
        total += num
    print(f"  Sum before 0: {total}")
    
    # Continue example
    print("\nSkip odd numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(f"  {i}", end=" ")
    print()
    print()


# =============================================================================
# EXERCISE 5: FUNCTIONS
# =============================================================================

def add_numbers(a, b):
    """Add two numbers and return result."""
    return a + b


def greet(name, greeting="Hello"):
    """Greet a person with optional greeting."""
    return f"{greeting}, {name}!"


def sum_all(*args):
    """Sum all arguments."""
    return sum(args)


def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def exercise_5_functions():
    """Practice with functions."""
    print("=== Exercise 5: Functions ===")
    
    # Test all functions
    print(f"Add: {add_numbers(5, 3)}")
    print(f"Greet: {greet('Alice')}")
    print(f"Greet with custom: {greet('Bob', 'Hi')}")
    print(f"Sum all: {sum_all(1, 2, 3, 4, 5)}")
    print("Info:")
    print_info(name="Bob", age=30, city="NYC")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 0: {factorial(0)}")
    
    # Lambda function
    square = lambda x: x**2
    print(f"Square of 7 (lambda): {square(7)}")
    print()


# =============================================================================
# EXERCISE 6: CLASSES
# =============================================================================

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def years_until_retirement(self, retirement_age=65):
        """Calculate years until retirement."""
        years = retirement_age - self.age
        return years if years > 0 else 0


class Student(Person):
    """A Student class that inherits from Person."""
    
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
    
    def introduce(self):
        """Override introduce for student."""
        return f"Hi, I'm {self.name}, student ID: {self.student_id}, grade: {self.grade}"


def exercise_6_classes():
    """Practice with classes."""
    print("=== Exercise 6: Classes ===")
    
    # Create Person instance
    person = Person("Alice", 30)
    print(f"Person intro: {person.introduce()}")
    print(f"Years until retirement: {person.years_until_retirement()}")
    
    # Create Student instance
    student = Student("Bob", 20, "S12345", "A")
    print(f"Student intro: {student.introduce()}")
    print(f"Years until retirement: {student.years_until_retirement()}")
    print()


# =============================================================================
# EXERCISE 7: FILE OPERATIONS
# =============================================================================

def read_file(file_path):
    """Read file and return contents."""
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, content):
    """Write content to file."""
    with open(file_path, 'w') as f:
        f.write(content)


def append_file(file_path, content):
    """Append content to file."""
    with open(file_path, 'a') as f:
        f.write(content)


def exercise_7_file_operations():
    """Practice with file operations."""
    print("=== Exercise 7: File Operations ===")
    
    import os
    
    # Test file operations
    test_file = "test_file.txt"
    
    # Write
    write_file(test_file, "Hello, World!\n")
    print("Written to file")
    
    # Read
    content = read_file(test_file)
    print(f"Read from file: {content.strip()}")
    
    # Append
    append_file(test_file, "This is appended.\n")
    print("Appended to file")
    
    # Read again
    content = read_file(test_file)
    print(f"Final content: {content.strip()}")
    
    # Cleanup
    os.remove(test_file)
    print("File deleted")
    print()


# =============================================================================
# EXERCISE 8: EXCEPTION HANDLING
# =============================================================================

def safe_divide(a, b):
    """Divide two numbers safely with exception handling."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid types"


def safe_read_file(file_path):
    """Read file safely with exception handling."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        print("File read successfully!")
    finally:
        print("File operation completed")


def exercise_8_exceptions():
    """Practice with exception handling."""
    print("=== Exercise 8: Exception Handling ===")
    
    # Test exception handling
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"'10' / 2 = {safe_divide('10', 2)}")
    
    # Test file exception handling
    print("\nFile operations:")
    result = safe_read_file("nonexistent_file.txt")
    print(f"Result: {result}")
    print()


# =============================================================================
# EXERCISE 9: STRING MANIPULATION
# =============================================================================

def exercise_9_strings():
    """Practice with string manipulation."""
    print("=== Exercise 9: String Manipulation ===")
    
    text = "Hello, World! Python is awesome."
    
    # Find substring
    python_index = text.find("Python")
    print(f"Python found at index: {python_index}")
    
    # Replace substring
    replaced = text.replace("World", "Universe")
    print(f"Replaced: {replaced}")
    
    # Check if string starts/ends with
    print(f"Starts with 'Hello': {text.startswith('Hello')}")
    print(f"Ends with 'awesome.': {text.endswith('awesome.')}")
    
    # Count occurrences
    o_count = text.count('o')
    print(f"Count of 'o': {o_count}")
    
    # Split and join
    words = text.split()
    joined = "-".join(words)
    print(f"Joined: {joined}")
    
    # Check if alphanumeric
    print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")
    print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")
    print(f"'123'.isdigit(): {'123'.isdigit()}")
    print()


# =============================================================================
# EXERCISE 10: ENUMERATE & ZIP
# =============================================================================

def exercise_10_enumerate_zip():
    """Practice with enumerate and zip."""
    print("=== Exercise 10: Enumerate & Zip ===")
    
    # Use enumerate
    fruits = ["apple", "banana", "cherry"]
    print("Fruits with index:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # Use zip
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    print("\nNames and ages:")
    for name, age in zip(names, ages):
        print(f"  {name}: {age}")
    
    # Create dictionary from two lists
    name_age_dict = dict(zip(names, ages))
    print(f"\nDictionary: {name_age_dict}")
    
    # Zip three lists
    cities = ["NYC", "LA", "Chicago"]
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}, {age}, {city}")
    print()


# =============================================================================
# EXERCISE 11: MAP, FILTER, REDUCE
# =============================================================================

def exercise_11_map_filter():
    """Practice with map, filter, and reduce."""
    print("=== Exercise 11: Map, Filter, Reduce ===")
    
    from functools import reduce
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Use map to square all numbers
    squares = list(map(lambda x: x**2, numbers))
    print(f"Squares: {squares}")
    
    # Use filter to get even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Evens: {evens}")
    
    # Use map to convert strings to uppercase
    words = ["hello", "world", "python"]
    upper_words = list(map(str.upper, words))
    print(f"Uppercase: {upper_words}")
    
    # Use filter to remove empty strings
    mixed = ["hello", "", "world", "", "python"]
    non_empty = list(filter(lambda x: x, mixed))
    print(f"Non-empty: {non_empty}")
    
    # Use reduce to sum all numbers
    total = reduce(lambda x, y: x + y, numbers)
    print(f"Sum (reduce): {total}")
    print()


# =============================================================================
# EXERCISE 12: LIST SORTING
# =============================================================================

def exercise_12_sorting():
    """Practice with list sorting."""
    print("=== Exercise 12: List Sorting ===")
    
    # Sort numbers
    numbers = [5, 2, 8, 1, 9, 3]
    numbers_asc = sorted(numbers)
    numbers_desc = sorted(numbers, reverse=True)
    print(f"Ascending: {numbers_asc}")
    print(f"Descending: {numbers_desc}")
    
    # Sort strings case-insensitively
    names = ["Alice", "bob", "Charlie", "alice"]
    names_sorted = sorted(names, key=str.lower)
    print(f"Case-insensitive: {names_sorted}")
    
    # Sort list of dictionaries by key
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    people_sorted = sorted(people, key=lambda x: x["age"])
    print(f"Sorted by age: {people_sorted}")
    
    # sorted() vs list.sort()
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f"Original: {numbers}")
    print(f"After sort(): {numbers_copy}")
    print()


# =============================================================================
# EXERCISE 13: WORKING WITH DATES
# =============================================================================

def exercise_13_dates():
    """Practice with datetime module."""
    print("=== Exercise 13: Working with Dates ===")
    
    from datetime import datetime, timedelta
    
    # Get current date and time
    now = datetime.now()
    print(f"Current datetime: {now}")
    
    # Format date as string
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted: {formatted}")
    
    # Parse string to date
    date_str = "2024-01-15"
    parsed = datetime.strptime(date_str, "%Y-%m-%d")
    print(f"Parsed: {parsed}")
    
    # Calculate date difference
    date1 = datetime(2024, 1, 1)
    date2 = datetime(2024, 12, 31)
    diff = date2 - date1
    print(f"Days between: {diff.days}")
    
    # Add/subtract days
    future = now + timedelta(days=30)
    past = now - timedelta(days=7)
    print(f"30 days later: {future.strftime('%Y-%m-%d')}")
    print(f"7 days ago: {past.strftime('%Y-%m-%d')}")
    print()


# =============================================================================
# EXERCISE 14: JSON OPERATIONS
# =============================================================================

def exercise_14_json():
    """Practice with JSON operations."""
    print("=== Exercise 14: JSON Operations ===")
    
    import json
    
    # Convert Python dict to JSON string
    data = {"name": "Alice", "age": 25, "city": "NYC"}
    json_str = json.dumps(data)
    print(f"Dict to JSON: {json_str}")
    
    # Convert JSON string to Python dict
    json_str = '{"name": "Bob", "age": 30}'
    parsed_data = json.loads(json_str)
    print(f"JSON to dict: {parsed_data}")
    
    # Write Python dict to JSON file
    with open("test.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Written to test.json")
    
    # Read JSON file to Python dict
    with open("test.json", "r") as f:
        loaded_data = json.load(f)
    print(f"Loaded from file: {loaded_data}")
    
    # Handle nested structures
    nested = {"person": {"name": "Charlie", "address": {"city": "LA"}}}
    nested_json = json.dumps(nested, indent=2)
    print(f"Nested JSON: {nested_json}")
    
    # Cleanup
    import os
    os.remove("test.json")
    print("File deleted")
    print()


# =============================================================================
# EXERCISE 15: REGULAR EXPRESSIONS BASICS
# =============================================================================

def exercise_15_regex():
    """Practice with regular expressions."""
    print("=== Exercise 15: Regular Expressions ===")
    
    import re
    
    # Search for pattern in string
    text = "Contact us at support@example.com or sales@example.com"
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    print(f"Emails found: {emails}")
    
    # Validate phone number format
    phone = "123-456-7890"
    pattern = r'\d{3}-\d{3}-\d{4}'
    is_valid = re.match(pattern, phone)
    print(f"Phone valid: {is_valid is not None}")
    
    # Replace pattern in string
    text2 = "Hello World, Hello Python"
    replaced = re.sub(r'Hello', 'Hi', text2)
    print(f"Replaced: {replaced}")
    
    # Split string by pattern
    text3 = "apple,banana;cherry|date"
    parts = re.split(r'[,\;|]', text3)
    print(f"Split: {parts}")
    print()


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    """Run all exercises."""
    print("=" * 60)
    print("PYTHON CORE CONCEPTS REVISION - DAY 0")
    print("=" * 60)
    print()
    
    exercise_1_data_types()
    exercise_2_lists()
    exercise_3_dictionaries()
    exercise_4_control_flow()
    exercise_5_functions()
    exercise_6_classes()
    exercise_7_file_operations()
    exercise_8_exceptions()
    exercise_9_strings()
    exercise_10_enumerate_zip()
    exercise_11_map_filter()
    exercise_12_sorting()
    exercise_13_dates()
    exercise_14_json()
    exercise_15_regex()
    
    print("=" * 60)
    print("All exercises completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
