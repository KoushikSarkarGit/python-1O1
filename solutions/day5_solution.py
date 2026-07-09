"""
Day 5: Advanced OOP & Magic Methods
Project: Build a Custom DataFrame Class - SOLUTION
"""

from typing import Dict, List, Any, Callable, Union


class DataFrame:
    """A mini pandas-like DataFrame implementation."""
    
    def __init__(self, data: Dict[str, List[Any]]):
        self.data = data
        self._validate_columns()
    
    def _validate_columns(self):
        """Validate that all columns have the same length."""
        if not self.data:
            return
        lengths = [len(col) for col in self.data.values()]
        if len(set(lengths)) > 1:
            raise ValueError("All columns must have the same length")
    
    def __getitem__(self, key: Union[int, str, slice]) -> Union[Dict[str, Any], List[Any], 'DataFrame']:
        if isinstance(key, int):
            return {col: self.data[col][key] for col in self.data}
        elif isinstance(key, str):
            return self.data[key]
        elif isinstance(key, slice):
            new_data = {col: self.data[col][key] for col in self.data}
            return DataFrame(new_data)
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __setitem__(self, key: Union[str, tuple], value: Union[List[Any], Any]):
        if isinstance(key, str):
            if len(value) != len(next(iter(self.data.values()))):
                raise ValueError("Column length must match existing columns")
            self.data[key] = value
        elif isinstance(key, tuple) and len(key) == 2:
            row_idx, col_name = key
            self.data[col_name][row_idx] = value
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __add__(self, other: 'DataFrame') -> 'DataFrame':
        if self.data.keys() != other.data.keys():
            raise ValueError("DataFrames must have same columns")
        new_data = {}
        for col in self.data:
            new_data[col] = [a + b for a, b in zip(self.data[col], other.data[col])]
        return DataFrame(new_data)
    
    def __sub__(self, other: 'DataFrame') -> 'DataFrame':
        if self.data.keys() != other.data.keys():
            raise ValueError("DataFrames must have same columns")
        new_data = {}
        for col in self.data:
            new_data[col] = [a - b for a, b in zip(self.data[col], other.data[col])]
        return DataFrame(new_data)
    
    def __len__(self) -> int:
        if not self.data:
            return 0
        return len(next(iter(self.data.values())))
    
    def __bool__(self) -> bool:
        return len(self) > 0
    
    def __str__(self) -> str:
        if not self.data:
            return "Empty DataFrame"
        lines = [f"  {col}" for col in self.data.keys()]
        for i in range(min(3, len(self))):
            lines.append(f"  {i}: {self[i]}")
        return "DataFrame:\n" + "\n".join(lines)
    
    def __repr__(self) -> str:
        return f"DataFrame(columns={list(self.data.keys())}, rows={len(self)})"
    
    @property
    def shape(self) -> tuple:
        return (len(self), len(self.data))
    
    @property
    def columns(self) -> List[str]:
        return list(self.data.keys())
    
    def __call__(self, func: Callable[[Any], Any]) -> 'DataFrame':
        new_data = {}
        for col in self.data:
            new_data[col] = [func(val) for val in self.data[col]]
        return DataFrame(new_data)


def main():
    print("=== Custom DataFrame Class ===\n")

    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 70000]
    }
    df = DataFrame(data)
    print(f"1. Created DataFrame with shape: {df.shape}")
    print(f"   Columns: {df.columns}\n")

    print(f"2. First row: {df[0]}")
    print(f"   Name column: {df['name']}\n")

    df['bonus'] = [5000, 6000, 7000]
    print(f"3. Added bonus column: {df.columns}")
    df[0, 'age'] = 26
    print(f"   Modified first row age: {df[0]}\n")

    df2 = DataFrame({'salary': [10000, 15000, 20000], 'bonus': [1000, 1500, 2000]})
    df3 = df + df2
    print(f"4. Addition result shape: {df3.shape}\n")

    print(f"5. Length: {len(df)}")
    print(f"   Bool: {bool(df)}\n")

    print("6. String representation:")
    print(df)

    print("\n7. Callable:")
    doubled = df(lambda x: x * 2 if isinstance(x, (int, float)) else x)
    print(f"   Doubled numeric values")


if __name__ == "__main__":
    main()
