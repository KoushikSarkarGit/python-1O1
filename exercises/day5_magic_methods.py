"""
Day 5: Advanced OOP & Magic Methods
Project: Build a Custom DataFrame Class

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand magic methods (dunder methods) in Python
- Implement __getitem__, __setitem__ for custom indexing
- Implement __add__, __sub__ for operator overloading
- Implement __len__, __bool__ for validation
- Use property decorators for computed attributes
- Implement __call__ to make objects callable
- Build a mini pandas-like DataFrame from scratch

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a custom DataFrame class that mimics basic pandas functionality:
1. Store data in a dictionary of columns
2. Support indexing with [] notation
3. Support arithmetic operations (+, -)
4. Support len() and bool() operations
5. Provide computed columns via properties
6. Make the DataFrame callable to apply functions

=============================================================================
MAGIC METHODS CONCEPTS:
=============================================================================
Magic methods (dunder methods) allow you to define how objects behave
with Python's built-in operations.

Common magic methods:
- __getitem__/__setitem__: Enable obj[key] syntax
- __add__/__sub__: Enable + and - operators
- __len__: Enable len(obj) function
- __bool__: Enable bool(obj) conversion
- __str__/__repr__: Enable string representation
- __call__: Enable obj() callable syntax
- __eq__/__lt__: Enable comparison operators

Property decorators:
- @property: Create getter methods accessed as attributes
- @setter: Create setter methods for properties

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. __init__(self, data: Dict[str, List])
   - Store data as dictionary of columns
   - Validate that all columns have same length
   - Store column names and row count

2. __getitem__(self, key)
   - Support integer indexing (df[0] returns row as dict)
   - Support string indexing (df['name'] returns column)
   - Support slicing (df[0:2] returns subset)
   - Raise KeyError for invalid keys

3. __setitem__(self, key, value)
   - Support setting entire column (df['new_col'] = [1, 2, 3])
   - Support setting single cell (df[0, 'name'] = 'Bob')
   - Validate length matches existing columns

4. __add__(self, other)
   - Support adding two DataFrames
   - Add corresponding columns element-wise
   - Return new DataFrame with result
   - Raise ValueError if shapes don't match

5. __sub__(self, other)
   - Support subtracting two DataFrames
   - Subtract corresponding columns element-wise
   - Return new DataFrame with result
   - Raise ValueError if shapes don't match

6. __len__(self)
   - Return number of rows
   - Enables len(df) syntax

7. __bool__(self)
   - Return True if DataFrame has data
   - Return False if DataFrame is empty
   - Enables if df: syntax

8. __str__(self) and __repr__(self)
   - __str__: User-friendly string representation
   - __repr__: Developer-friendly representation
   - Show column names and first few rows

9. @property shape
   - Return tuple of (rows, columns)
   - Computed property (no storage needed)

10. @property columns
    - Return list of column names
    - Computed property

11. __call__(self, func)
    - Apply function to all columns
    - Return new DataFrame with transformed data
    - Enables df(func) syntax

=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests all magic methods:
1. Creation - Initialize DataFrame with data
2. Indexing - Get rows and columns
3. Setting - Add new columns and modify cells
4. Arithmetic - Add and subtract DataFrames
5. Built-in functions - len() and bool()
6. String representation - print(df)
7. Properties - df.shape and df.columns
8. Callable - Apply functions with df(func)

Expected behavior:
- df[0] returns first row as dictionary
- df['name'] returns name column
- df1 + df2 adds corresponding values
- len(df) returns number of rows
- bool(df) returns True if not empty
- df(lambda x: x * 2) doubles all values

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Implement __eq__ for DataFrame comparison
- Implement __iter__ to iterate over rows
- Implement __contains__ to check if column exists
- Add @property for mean, max, min of numeric columns
- Implement __mul__ and __truediv__ operators
- Add method to filter rows based on condition
- Implement pivot table functionality
"""

from typing import Dict, List, Any, Callable, Union


class DataFrame:
    """A mini pandas-like DataFrame implementation."""
    
    def __init__(self, data: Dict[str, List[Any]]):
        # TODO: Store data, validate column lengths
        pass
    
    def __getitem__(self, key: Union[int, str, slice]) -> Union[Dict[str, Any], List[Any], 'DataFrame']:
        # TODO: Implement indexing for int, str, and slice
        pass
    
    def __setitem__(self, key: Union[str, tuple], value: Union[List[Any], Any]):
        # TODO: Implement setting columns and cells
        pass
    
    def __add__(self, other: 'DataFrame') -> 'DataFrame':
        # TODO: Implement DataFrame addition
        pass
    
    def __sub__(self, other: 'DataFrame') -> 'DataFrame':
        # TODO: Implement DataFrame subtraction
        pass
    
    def __len__(self) -> int:
        # TODO: Return number of rows
        pass
    
    def __bool__(self) -> bool:
        # TODO: Return True if DataFrame has data
        pass
    
    def __str__(self) -> str:
        # TODO: Return user-friendly string representation
        pass
    
    def __repr__(self) -> str:
        # TODO: Return developer-friendly representation
        pass
    
    @property
    def shape(self) -> tuple:
        # TODO: Return (rows, columns) tuple
        pass
    
    @property
    def columns(self) -> List[str]:
        # TODO: Return list of column names
        pass
    
    def __call__(self, func: Callable[[Any], Any]) -> 'DataFrame':
        # TODO: Apply function to all columns
        pass


def main():
    print("=== Custom DataFrame Class ===\n")

    # Test creation
    print("1. Testing DataFrame creation:")
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 70000]
    }
    df = DataFrame(data)
    print(f"  Created DataFrame with shape: {df.shape}")
    print(f"  Columns: {df.columns}\n")

    # Test indexing
    print("2. Testing indexing:")
    print(f"  First row: {df[0]}")
    print(f"  Name column: {df['name']}\n")

    # Test setting
    print("3. Testing setting:")
    df['bonus'] = [5000, 6000, 7000]
    print(f"  Added bonus column: {df.columns}")
    df[0, 'age'] = 26
    print(f"  Modified first row age: {df[0]}\n")

    # Test arithmetic
    print("4. Testing arithmetic:")
    df2 = DataFrame({'salary': [10000, 15000, 20000], 'bonus': [1000, 1500, 2000]})
    df3 = df + df2
    print(f"  Addition result shape: {df3.shape}\n")

    # Test built-in functions
    print("5. Testing built-in functions:")
    print(f"  Length: {len(df)}")
    print(f"  Bool: {bool(df)}\n")

    # Test string representation
    print("6. Testing string representation:")
    print(df)

    # Test callable
    print("\n7. Testing callable:")
    doubled = df(lambda x: x * 2 if isinstance(x, (int, float)) else x)
    print(f"  Doubled numeric values")


if __name__ == "__main__":
    main()
