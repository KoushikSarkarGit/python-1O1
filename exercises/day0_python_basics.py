"""
Day 0: Python Core Concepts Revision
Project: Comprehensive Basics Refresher

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Refresh knowledge of Python data types and structures
- Practice control flow (if/else, loops)
- Reinforce function concepts (parameters, return values, default args)
- Review basic class and object-oriented programming
- Practice file I/O operations
- Understand exception handling basics
- Warm up for advanced topics in Week 1

=============================================================================
PROJECT OVERVIEW:
=============================================================================
This is a comprehensive revision day covering all Python basics you should know
before starting the advanced 2-week course. Complete these exercises to ensure
you have a solid foundation for the upcoming advanced topics.

=============================================================================
EXERCISES TO COMPLETE:
=============================================================================

1. DATA TYPES & OPERATIONS
   - Create variables of different types (int, float, str, bool)
   - Perform type conversions (int(), str(), float(), bool())
   - Use string methods (upper(), lower(), strip(), split(), join())
   - Practice string formatting (f-strings, format(), %)
   - Work with numbers (arithmetic, comparison, logical operators)

2. LISTS & TUPLES
   - Create and access list elements
   - List methods: append(), extend(), insert(), remove(), pop()
   - List slicing and indexing
   - List comprehensions
   - Create and access tuples
   - Understand tuple immutability
   - Unpack tuples

3. DICTIONARIES & SETS
   - Create and access dictionary values
   - Dictionary methods: keys(), values(), items(), get()
   - Add, update, delete dictionary items
   - Dictionary comprehensions
   - Create sets and perform set operations
   - Set methods: add(), remove(), union(), intersection()

4. CONTROL FLOW
   - if/elif/else statements
   - Comparison operators (==, !=, <, >, <=, >=)
   - Logical operators (and, or, not)
   - for loops with range() and iterables
   - while loops
   - break, continue, pass statements
   - Nested loops

5. FUNCTIONS
   - Define functions with parameters
   - Default parameter values
   - *args and **kwargs
   - Return values (single and multiple)
   - Lambda functions
   - Function scope (local vs global)
   - Recursion basics

6. CLASSES & OBJECTS
   - Define a class with __init__ method
   - Create instance attributes
   - Define instance methods
   - Understand self parameter
   - Class attributes vs instance attributes
   - Basic inheritance

7. FILE OPERATIONS
   - Open files in different modes (r, w, a)
   - Read files (read(), readline(), readlines())
   - Write to files (write(), writelines())
   - Use context managers (with statement)
   - Handle file paths with os.path

8. EXCEPTION HANDLING
   - try/except blocks
   - Catch specific exceptions
   - else and finally blocks
   - Raise custom exceptions
   - Handle multiple exceptions

=============================================================================
DETAILED EXERCISES:
=============================================================================

Exercise 1: Data Types
    a) Create variables: age (int), price (float), name (str), is_active (bool)
    b) Convert age to string and concatenate with name
    c) Convert price string to float and calculate discount
    d) Use string methods to clean user input

Exercise 2: Lists
    a) Create a list of numbers [1, 2, 3, 4, 5]
    b) Add 6 to the end of the list
    c) Insert 0 at the beginning
    d) Remove the number 3
    e) Reverse the list
    f) Use list comprehension to create squares of numbers 1-10

Exercise 3: Dictionaries
    a) Create a dictionary for a person (name, age, city)
    b) Add email to the dictionary
    c) Update the age
    d) Get the city using .get() with default value
    e) Print all keys and values
    f) Use dict comprehension to create {num: num*2 for num in range(5)}

Exercise 4: Control Flow
    a) Write a function to check if a number is positive, negative, or zero
    b) Use for loop to print even numbers from 1-20
    c) Use while loop to sum numbers until user enters 0
    d) Break out of loop when condition is met
    e) Use continue to skip odd numbers

Exercise 5: Functions
    a) Write a function that takes two numbers and returns sum
    b) Write a function with default parameter value
    c) Write a function that accepts *args
    d) Write a function that accepts **kwargs
    e) Write a lambda function to square a number
    f) Write a recursive function to calculate factorial

Exercise 6: Classes
    a) Create a Person class with name and age attributes
    b) Add a method to introduce the person
    c) Add a method to calculate years until retirement (age 65)
    d) Create a Student class that inherits from Person
    e) Add student_id and grade attributes to Student
    f) Override the introduce method for Student

Exercise 7: File Operations
    a) Write a function to read a file and return its contents
    b) Write a function to write data to a file
    c) Write a function to append data to a file
    d) Use context manager for file operations
    e) Handle file not found errors

Exercise 8: Exception Handling
    a) Write a function that divides two numbers with try/except
    b) Handle ZeroDivisionError specifically
    c) Handle FileNotFoundError when opening files
    d) Use else block to execute code when no exception occurs
    e) Use finally block to ensure cleanup

=============================================================================
TESTING YOUR CODE:
=============================================================================
Run the main() function to test all exercises.
Expected output:
- All data type operations work correctly
- List manipulations produce expected results
- Dictionary operations work as expected
- Control flow statements execute correctly
- Functions return correct values
- Class instances work properly
- File operations succeed
- Exceptions are caught and handled

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Create a function that accepts any iterable and returns a list
- Implement a simple linked list class
- Create a decorator that times function execution
- Write a context manager for temporary directory
- Implement a simple stack class using list
- Create a function that merges two dictionaries
"""

# =============================================================================
# EXERCISE 1: DATA TYPES
# =============================================================================

def exercise_1_data_types():
    """Practice with data types and operations."""
    print("=== Exercise 1: Data Types ===")
    
    # TODO: Create variables of different types
    age = 1  # int
    price = 9.99  # float
    name = "Koushik" # str
    is_active = True  # bool
    
    # TODO: Type conversions
    # Convert age to string and concatenate with name
    # Convert price string to float
    
    # TODO: String methods
    text = "  Hello World  "
    # Use strip(), upper(), lower(), split()
    
    # TODO: String formatting with f-strings
    # Format: "Name: {name}, Age: {age}, Price: ${price:.2f}"
    
    print(f"Name: {name}, Age: {age}, Price: ${price:.2f}, isActive: {is_active} ")
    print()


# =============================================================================
# EXERCISE 2: LISTS & TUPLES
# =============================================================================

def exercise_2_lists():
    """Practice with lists and tuples."""
    print("=== Exercise 2: Lists & Tuples ===")
    
    # TODO: Create a list of numbers
    numbers = [1,2,3,4]
    
    # TODO: List operations
    # Add 6 to the end
    # Insert 0 at the beginning
    # Remove the number 3
    # Reverse the list
    numbers.append(6)
    numbers.insert(0,0)
    numbers.remove(3)
    numbers.reverse()
    # TODO: List comprehension
    # Create squares of numbers 1-10
    squares = []
    for a in range(10) :
        squares.append((a+1)**2)
    
    # TODO: Create a tuple
    coordinates = (1,2,3)
    
    # TODO: Tuple unpacking
    x, y, z = coordinates
    
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    print(f"Coordinates: {coordinates}")
    print()

# =============================================================================
# EXERCISE 3: DICTIONARIES & SETS
# =============================================================================

def exercise_3_dictionaries():
    """Practice with dictionaries and sets."""
    print("=== Exercise 3: Dictionaries & Sets ===")
    
    # TODO: Create a dictionary for a person
    person = {}
    
    # TODO: Dictionary operations
    # Add email
    # Update age
    # Get city with default value
    # Print all keys and values
    person["email"] = "sarkarkoushik557@gmail.com"
    person["age"] = 24
    city = person.get("city", "Default City")
    print(f"{list(person.keys())}")
    print(f"{list(person.items())}")
    
    # TODO: Dictionary comprehension
    # Create {num: num*2 for num in range(5)}
    doubled = {"num": k**2 for k in range(5)}
    
    # TODO: Create a set
    unique_numbers = {1,2,3,1,2}
    print(f"Unique Numbers: {unique_numbers}")
    # TODO: Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    # Find union and intersection
    unionset = set1 | set2
    print(f"Person: {person}")
    print(f"Doubled: {doubled}")
    print(f"Union: {unionset}")
    print(f"Intersection: {set1 & set2}")
    print()

# =============================================================================
# EXERCISE 4: CONTROL FLOW
# =============================================================================

def check_number(num):
    """Check if a number is positive, negative, or zero."""
    # TODO: Implement using if/elif/else
    if num == 0 :
        return "Zero"
    elif num > 0 :
        return "Positive"
    else :
        return "Negative"


def exercise_4_control_flow():
    """Practice with control flow."""
    print("=== Exercise 4: Control Flow ===")
    
    # TODO: Test check_number function
    print(f"5 is: {check_number(5)}")
    print(f"-3 is: {check_number(-3)}")
    print(f"0 is: {check_number(0)}")
    
    # TODO: For loop - print even numbers 1-20
    ans = [x & (x%2 ==0) for x in range(1,20)]
    print(f"{ ans }")
    # TODO: While loop example
    x=0;
    while x <5 :
        x += 1
        print(x)
    # TODO: Break and continue examples
    y = 5
    while True :
        if y >7:
            break
        elif y <2:
            continue
        else : 
            print(f"printing: {y}")
            y += 1

    print()


# =============================================================================
# EXERCISE 5: FUNCTIONS
# =============================================================================

def add_numbers(a, b):
    """Add two numbers and return result."""
    # TODO: Implement
    return (a+b)

print(add_numbers(3, 5))

def greet(name, greeting="Hello"):
    """Greet a person with optional greeting."""
    # TODO: Implement with default parameter
    print(f"{greeting} {name}")


def sum_all(*args):
    """Sum all arguments."""
    # TODO: Implement with *args
    sum = 0
    for item in args:
        sum += item


    return sum



def print_info(**kwargs):
    """Print all keyword arguments."""
    # TODO: Implement with **kwargs
    print([item for item in kwargs.values()])
    print(kwargs)




def factorial(n):
    """Calculate factorial recursively."""
    # TODO: Implement recursively
    if n <= 1 :
        return 1;
    return n* factorial(n-1);



def exercise_5_functions():
    """Practice with functions."""
    print("=== Exercise 5: Functions ===")
    
    # TODO: Test all functions
    print(f"Add: {add_numbers(5, 3)}")
    print(f"Greet: {greet('Alice')}")
    print(f"Sum all: {sum_all(1, 2, 3, 4, 5)}")
    print_info(name="Bob", age=30, city="NYC")
    print(f"Factorial of 5: {factorial(5)}")
    print()

exercise_5_functions()
# =============================================================================
# EXERCISE 6: CLASSES
# =============================================================================

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        # TODO: Initialize attributes
        self.name = name
        self.age = age
    
    def introduce(self):
        """Introduce the person."""
        # TODO: Return introduction string
        print(f"Hi! My name is {self.name} and I am {self.age} year{"s" if self.age >1 else "" } old")
    
    def years_until_retirement(self, retirement_age=65):
        """Calculate years until retirement."""
        # TODO: Implement
        years = 60- self.age
        print(f"I have {years} Year{"s" if years >0 else ""} till I retire")

# myperson = Person("Koushik", 24);

# myperson.introduce()
# myperson.years_until_retirement()

class Student(Person):
    """A Student class that inherits from Person."""
    
    def __init__(self, name, age, student_id, grade):
        # TODO: Initialize with parent and student attributes
       super().__init__(name, age)
       self.student_id = student_id
       self.grade = grade
    
    def introduce(self):
        """Override introduce for student."""
        # TODO: Override parent method
        print(self.__dict__)
        super().introduce()

mystudent = Student("Jeet", 24, 123456, "A+")
mystudent.introduce()



def exercise_6_classes():
    """Practice with classes."""
    print("=== Exercise 6: Classes ===")
    
    # TODO: Create Person instance and test methods
    # TODO: Create Student instance and test methods
    print()


# =============================================================================
# EXERCISE 7: FILE OPERATIONS
# =============================================================================

def read_file(file_path):
    """Read file and return contents."""
    # TODO: Implement with context manager
    with open(file_path, 'r') as myfile:
        print(myfile.read())

read_file("./SampleData/DummyData.txt")




def write_file(file_path, content):
    """Write content to file."""
    # TODO: Implement with context manager
    with open(file_path, 'w') as f:
        f.write(content)

write_file( "./SampleData/DummyData.txt", "New Content" )
          

def append_file(file_path, content):
    """Append content to file."""
    # TODO: Implement with context manager
    pass


def exercise_7_file_operations():
    """Practice with file operations."""
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
    # TODO: Implement with try/except
    try:
       return a/b
    except ZeroDivisionError:
        print("Division by 0 not allowed")
    except TypeError:
        print("Typ Error")


def safe_read_file(file_path):
    """Read file safely with exception handling."""
    # TODO: Implement with try/except/else/finally
    pass


def exercise_8_exceptions():
    """Practice with exception handling."""
    print("=== Exercise 8: Exception Handling ===")
    
    # TODO: Test exception handling
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print()

exercise_8_exceptions()
# =============================================================================
# EXERCISE 9: STRING MANIPULATION
# =============================================================================

def exercise_9_strings():
    """Practice with string manipulation."""
    print("=== Exercise 9: String Manipulation ===")
    
    # TODO: String operations
    text = "Hello, World! Python is awesome."
    
    # Find substring
    # TODO: Use find() to find "Python"
    text.find("python")
    # Replace substring
    # TODO: Use replace() to replace "World" with "Universe"

    replaced = text.replace("World" ,"Universe", 1)
    print(replaced)
    # Check if string starts/ends with
    # TODO: Use startswith() and endswith()
    check = text.startswith("He") & text.endswith("ome")
    print(check)
    # Count occurrences
    # TODO: Use count() to count 'o'
    print (f" o count : {text.count("o", 0,5)}")
    # Split and join
    # TODO: Split by spaces, then join with '-'
    newtextlist= text.split(" ")
    newtext = "-".join(newtextlist)
    print(newtext)
    # Check if alphanumeric
    # TODO: Use isalnum(), isalpha(), isdigit()
    inputstr = "324dsfsd21@hgsd"
    print(f"is alphbetic :{inputstr.isalpha()} \n is number {inputstr.isalnum()} \n {inputstr.isdigit()}")

exercise_9_strings()
# =============================================================================
# EXERCISE 10: ENUMERATE & ZIP
# =============================================================================

def exercise_10_enumerate_zip():
    """Practice with enumerate and zip."""
    print("=== Exercise 10: Enumerate & Zip ===")
    
    # TODO: Use enumerate to get index and value
    # TODO: Print each fruit with its index
    fruits = ["apple", "banana", "cherry"]

    for index, item in enumerate(fruits):
        print(f"index: {index} value:{item}")

    
    
    # TODO: Use zip to iterate over two lists
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names,ages):
        print(f"person name: {name} age: {age}")
    # TODO: Print name and age together
    
    # TODO: Create dictionary from two lists using zip

# here if you give more than 2 list in zip and try to dict it, it will give error
    newdict =  dict(zip(names,ages))
    print(newdict)
    # TODO: Zip three lists together
    
    print()

exercise_10_enumerate_zip()

# =============================================================================
# EXERCISE 11: MAP, FILTER, REDUCE
# =============================================================================


import time

def exercise_11_map_filter():
    """Practice with map, filter, and reduce."""
    print("=== Exercise 11: Map, Filter, Reduce ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # TODO: Use map to square all numbers

    # apparently In Python 3, the map() function returns a map object, which is a lazy iterator.This iterator yields transformed items one by one on demand rather than storing the entire list in memory at once. (Note that in older versions like Python 2, map() used to return a literal list object)
    starttime = time.perf_counter()
    squared = map( lambda x  : x**2  , numbers)
    print(list(squared) )
    endtime = time.perf_counter()
    print(endtime - starttime )
    # TODO: Use filter to get even numbers
    # TODO: Use map to convert strings to uppercase
    words = ["hello", "world", "python"]
    UpperCase = list(map( lambda x  : x.upper()  , words))
    # TODO: Use filter to remove empty strings
    mixed = ["hello", "", "world", "", "python"]
    Filtered = list(map( lambda x  : x if x.strip() != "" else None  , words))
    # TODO: Use reduce to sum all numbers (from functools import reduce)
    print(Filtered)


    print()

exercise_11_map_filter()

# =============================================================================
# EXERCISE 12: LIST SORTING
# =============================================================================

def exercise_12_sorting():
    """Practice with list sorting."""
    print("=== Exercise 12: List Sorting ===")
    
    # TODO: Sort a list of numbers
    numbers = [5, 2, 8, 1, 9, 3]
    # TODO: Sort in ascending and descending order
    
    # TODO: Sort a list of strings
    names = ["Alice", "bob", "Charlie", "alice"]
    # TODO: Sort case-insensitively
    
    # TODO: Sort list of dictionaries by key
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    # TODO: Sort by age
    
    # TODO: Use sorted() vs list.sort()
    
    print()


# =============================================================================
# EXERCISE 13: WORKING WITH DATES
# =============================================================================

def exercise_13_dates():
    """Practice with datetime module."""
    print("=== Exercise 13: Working with Dates ===")
    
    from datetime import datetime, timedelta
    
    # TODO: Get current date and time
    curtime = datetime.now()
    # TODO: Format date as string
    strCurTime = curtime.strftime("%Y/%m/%d %H h %M min")
    print(strCurTime)
    # TODO: Parse string to date
    strToDate = datetime.strptime(strCurTime, "%Y/%m/%d %H h %M min")
    print(strToDate)
  
    # TODO: Add/subtract days from date
    # TODO: Calculate date difference
    today = curtime.date()
    prevday =  today - timedelta(days=1)

    diff = today - prevday
    print(type(diff),  diff)
    
    
    print()


# =============================================================================
# EXERCISE 14: JSON OPERATIONS
# =============================================================================

def exercise_14_json():
    """Practice with JSON operations."""
    print("=== Exercise 14: JSON Operations ===")
    
    import json
    
    # TODO: Convert Python dict to JSON string
    data = {"name": "Alice", "age": 25, "city": "NYC"}
    
    jsondata = json.load(data)
    print(jsondata)
    # TODO: Convert JSON string to Python dict
    json_str = '{"name": "Bob", "age": 30}'
    
    # TODO: Write Python dict to JSON file
    # TODO: Read JSON file to Python dict
    
    # TODO: Handle JSON with nested structures
    
    print()


# =============================================================================
# EXERCISE 15: REGULAR EXPRESSIONS BASICS
# =============================================================================

def exercise_15_regex():
    """Practice with regular expressions."""
    print("=== Exercise 15: Regular Expressions ===")
    
    import re
    
    # TODO: Search for pattern in string
    text = "Contact us at support@example.com or sales@example.com"
    # TODO: Find all email addresses
    
    # TODO: Validate phone number format
    phone = "123-456-7890"
    # TODO: Check if it matches pattern XXX-XXX-XXXX
    
    # TODO: Replace pattern in string
    # TODO: Split string by pattern
    
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
