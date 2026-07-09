"""
Day 7: File Operations & JSON/CSV Processing
Project: Build a Complete ETL Pipeline System - SOLUTION
"""

import csv
import json
import pathlib
import argparse
from typing import List, Dict, Any
from datetime import datetime
import time
import functools


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
        return all(field in record and record[field] for field in self.required_fields)
    
    def __contains__(self, field: str) -> bool:
        return field in self.required_fields


@timer
@logger
def extract_csv(file_path: str) -> List[Dict[str, Any]]:
    """Extract data from CSV file."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


@timer
@logger
def extract_json(file_path: str) -> List[Dict[str, Any]]:
    """Extract data from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


@timer
@logger
def extract_api(url: str) -> List[Dict[str, Any]]:
    """Extract data from API."""
    # Simulate API call
    return [{"id": 1, "name": "API Data"}]


def transform_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Transform data using comprehensions and generators."""
    transformed = []
    for record in data:
        clean_record = {}
        for key, value in record.items():
            if isinstance(value, str):
                clean_record[key] = value.strip()
                if clean_record[key].isdigit():
                    clean_record[key] = int(clean_record[key])
            else:
                clean_record[key] = value
        transformed.append(clean_record)
    return transformed


def validate_record(record: Dict[str, Any], validator: RecordValidator) -> bool:
    """Validate a single record."""
    return validator(record)


@timer
def load_csv(data: List[Dict[str, Any]], file_path: str):
    """Load data to CSV file."""
    with open(file_path, 'w', newline='') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


@timer
def load_json(data: List[Dict[str, Any]], file_path: str):
    """Load data to JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def run_etl_pipeline(sources: List[str], output_dir: str):
    """Run complete ETL pipeline."""
    all_data = []
    for source in sources:
        if source.endswith('.csv'):
            data = extract_csv(source)
        elif source.endswith('.json'):
            data = extract_json(source)
        else:
            continue
        all_data.extend(data)
    
    transformed = transform_data(all_data)
    validator = RecordValidator(['id', 'name'])
    valid_data = [r for r in transformed if validate_record(r, validator)]
    
    pathlib.Path(output_dir).mkdir(exist_ok=True)
    load_csv(valid_data, f"{output_dir}/output.csv")
    load_json(valid_data, f"{output_dir}/output.json")


def create_cli():
    """Create command-line interface."""
    parser = argparse.ArgumentParser(description="ETL Pipeline")
    parser.add_argument("--sources", nargs="+", required=True, help="Source files")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()
    run_etl_pipeline(args.sources, args.output)


def main():
    print("=== Complete ETL Pipeline ===\n")

    pathlib.Path("data").mkdir(exist_ok=True)
    
    sample_csv = """id,name,age,salary
1,Alice,25,50000
2,Bob,30,60000
3,Charlie,35,70000
"""
    with open("data/input.csv", "w") as f:
        f.write(sample_csv)
    print("1. Created data/input.csv")

    sample_json = [
        {"id": 4, "name": "David", "age": 28, "salary": 55000},
        {"id": 5, "name": "Eve", "age": 32, "salary": 65000}
    ]
    with open("data/input.json", "w") as f:
        json.dump(sample_json, f, indent=2)
    print("   Created data/input.json\n")

    print("2. Testing extraction:")
    csv_data = extract_csv("data/input.csv")
    json_data = extract_json("data/input.json")
    print(f"   Extracted {len(csv_data)} records from CSV")
    print(f"   Extracted {len(json_data)} records from JSON\n")

    print("3. Testing transformation:")
    all_data = csv_data + json_data
    transformed = transform_data(all_data)
    print(f"   Transformed {len(transformed)} records\n")

    print("4. Testing loading:")
    pathlib.Path("output").mkdir(exist_ok=True)
    load_csv(transformed, "output/output.csv")
    load_json(transformed, "output/output.json")
    print("   Created output files\n")


if __name__ == "__main__":
    main()
