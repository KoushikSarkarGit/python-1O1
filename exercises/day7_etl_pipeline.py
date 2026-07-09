"""
Day 7: File Operations & JSON/CSV Processing
Project: Build a Complete ETL Pipeline System

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Master advanced file operations with pathlib
- Handle JSON serialization/deserialization
- Process CSV files with csv module
- Combine all Week 1 concepts in a real project
- Build command-line interfaces
- Implement error handling and logging

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a complete ETL (Extract, Transform, Load) pipeline that:
1. Reads data from multiple sources (CSV, JSON, API)
2. Transforms data using comprehensions, generators, decorators
3. Validates data using custom classes with magic methods
4. Writes processed data to multiple formats
5. Adds logging using decorators
6. Handles errors with context managers
7. Provides a command-line interface

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. extract_csv(file_path: str) -> List[Dict]
   - Use csv.DictReader to read CSV
   - Apply @timer and @logger decorators
   - Return list of dictionaries
   - Handle file not found errors

2. extract_json(file_path: str) -> List[Dict]
   - Use json module to read JSON
   - Apply @timer and @logger decorators
   - Return list of dictionaries
   - Handle JSON decode errors

3. extract_api(url: str) -> List[Dict]
   - Use requests to fetch API data
   - Apply @timer and @logger decorators
   - Return list of dictionaries
   - Handle network errors

4. transform_data(data: List[Dict]) -> List[Dict]
   - Use comprehensions for transformation
   - Clean and normalize data
   - Apply validation with custom class
   - Use generators for memory efficiency

5. validate_record(record: Dict) -> bool
   - Use custom class with magic methods
   - Check required fields
   - Validate data types
   - Return True if valid

6. load_csv(data: List[Dict], file_path: str)
   - Write data to CSV file
   - Use csv.DictWriter
   - Apply @timer decorator

7. load_json(data: List[Dict], file_path: str)
   - Write data to JSON file
   - Use json.dump with indentation
   - Apply @timer decorator

8. run_etl_pipeline(sources: List[str], output_dir: str)
   - Orchestrate complete ETL process
   - Extract from all sources
   - Transform and validate
   - Load to multiple formats
   - Log progress

9. create_cli()
   - Use argparse for CLI
   - Accept source files and output directory
   - Run ETL pipeline
   - Handle CLI errors

=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests the complete pipeline:
1. Create sample CSV and JSON files
2. Extract data from both sources
3. Transform and validate
4. Load to output formats
5. Test CLI interface

Expected behavior:
- Data extracted from multiple sources
- Transformations applied correctly
- Invalid records filtered out
- Output files created in multiple formats
- CLI works with command-line arguments

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add parallel processing for multiple sources
- Implement incremental ETL (only process new data)
- Add data quality metrics
- Implement schema validation
- Add unit tests for each component
- Create configuration file support
"""

import csv
import json
import pathlib
import argparse
from typing import List, Dict, Any
from datetime import datetime
import time
import functools


# Reuse decorators from Day 2
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] {func.__name__} completed")
        return result
    return wrapper


class RecordValidator:
    """Custom class with magic methods for validation."""
    
    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields
    
    def __call__(self, record: Dict) -> bool:
        # TODO: Validate record has required fields
        pass
    
    def __contains__(self, field: str) -> bool:
        # TODO: Check if field is in required fields
        pass


@timer
@logger
def extract_csv(file_path: str) -> List[Dict[str, Any]]:
    """Extract data from CSV file."""
    # TODO: Implement CSV extraction
    pass


@timer
@logger
def extract_json(file_path: str) -> List[Dict[str, Any]]:
    """Extract data from JSON file."""
    # TODO: Implement JSON extraction
    pass


@timer
@logger
def extract_api(url: str) -> List[Dict[str, Any]]:
    """Extract data from API."""
    # TODO: Implement API extraction
    pass


def transform_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Transform data using comprehensions and generators."""
    # TODO: Implement data transformation
    pass


def validate_record(record: Dict[str, Any], validator: RecordValidator) -> bool:
    """Validate a single record."""
    # TODO: Implement validation
    pass


@timer
def load_csv(data: List[Dict[str, Any]], file_path: str):
    """Load data to CSV file."""
    # TODO: Implement CSV loading
    pass


@timer
def load_json(data: List[Dict[str, Any]], file_path: str):
    """Load data to JSON file."""
    # TODO: Implement JSON loading
    pass


def run_etl_pipeline(sources: List[str], output_dir: str):
    """Run complete ETL pipeline."""
    # TODO: Implement complete pipeline
    pass


def create_cli():
    """Create command-line interface."""
    # TODO: Implement CLI with argparse
    pass


def main():
    print("=== Complete ETL Pipeline ===\n")

    # Create sample data files
    print("1. Creating sample data files:")
    pathlib.Path("data").mkdir(exist_ok=True)
    
    sample_csv = """id,name,age,salary
1,Alice,25,50000
2,Bob,30,60000
3,Charlie,35,70000
"""
    with open("data/input.csv", "w") as f:
        f.write(sample_csv)
    print("  Created data/input.csv")

    sample_json = [
        {"id": 4, "name": "David", "age": 28, "salary": 55000},
        {"id": 5, "name": "Eve", "age": 32, "salary": 65000}
    ]
    with open("data/input.json", "w") as f:
        json.dump(sample_json, f, indent=2)
    print("  Created data/input.json\n")

    # Test extraction
    print("2. Testing extraction:")
    csv_data = extract_csv("data/input.csv")
    json_data = extract_json("data/input.json")
    print(f"  Extracted {len(csv_data)} records from CSV")
    print(f"  Extracted {len(json_data)} records from JSON\n")

    # Test transformation
    print("3. Testing transformation:")
    all_data = csv_data + json_data
    transformed = transform_data(all_data)
    print(f"  Transformed {len(transformed)} records\n")

    # Test loading
    print("4. Testing loading:")
    pathlib.Path("output").mkdir(exist_ok=True)
    load_csv(transformed, "output/output.csv")
    load_json(transformed, "output/output.json")
    print("  Created output files\n")

    # Test CLI
    print("5. Testing CLI:")
    # create_cli()


if __name__ == "__main__":
    main()
