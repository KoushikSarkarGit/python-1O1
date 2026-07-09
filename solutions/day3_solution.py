"""
Day 3: Generators & Iterators
Project: Build a Streaming Data Pipeline - SOLUTION
"""

from typing import Generator, Iterator, List, Dict, Any
import csv
from io import StringIO


def read_csv_in_chunks(file_path: str, chunk_size: int = 1000) -> Generator[List[Dict[str, str]], None, None]:
    """Generator that reads a large CSV file in chunks."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:  # Yield remaining rows
            yield chunk


def transform_data(data: Generator[List[Dict[str, str]], None, None]) -> Generator[Dict[str, Any], None, None]:
    """Generator that transforms data on-the-fly."""
    for chunk in data:
        for row in chunk:
            transformed = {}
            for key, value in row.items():
                # Clean whitespace
                cleaned_value = value.strip() if isinstance(value, str) else value
                # Convert numeric strings to integers
                if cleaned_value.isdigit():
                    transformed[key] = int(cleaned_value)
                else:
                    transformed[key] = cleaned_value
            yield transformed


def filter_valid_records(data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    """Generator that filters out invalid records."""
    for record in data:
        # Check if required fields are present and valid
        if 'id' in record and 'name' in record:
            if record['id'] and record['name']:
                yield record


class PaginatedAPIIterator:
    """Custom iterator for paginated API responses."""
    
    def __init__(self, total_items: int, page_size: int = 10):
        self.total_items = total_items
        self.page_size = page_size
        self.current_page = 0
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index >= self.total_items:
            raise StopIteration
        
        # Simulate fetching a page
        page_start = self.current_index
        page_end = min(self.current_index + self.page_size, self.total_items)
        page_data = list(range(page_start, page_end))
        
        self.current_index = page_end
        self.current_page += 1
        
        return {
            'page': self.current_page,
            'data': page_data,
            'has_more': self.current_index < self.total_items
        }


def build_etl_pipeline(data_source: str) -> Generator[Dict[str, Any], None, None]:
    """Chain generators to build a complete ETL pipeline."""
    # Chain: read -> transform -> filter
    raw_data = read_csv_in_chunks(data_source, chunk_size=100)
    transformed_data = transform_data(raw_data)
    clean_data = filter_valid_records(transformed_data)
    
    for record in clean_data:
        yield record


def main():
    print("=== Streaming Data Pipeline ===\n")

    # Create a temporary CSV file for testing
    import tempfile
    import os
    
    sample_csv = """id,name,age,salary
1,John,25,50000
2,Jane,30,60000
3,Bob,35,70000
4,Alice,,55000
5,Charlie,28,invalid
6,David,32,65000
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(sample_csv)
        temp_file = f.name
    
    try:
        print("1. Testing chunked CSV reading:")
        for i, chunk in enumerate(read_csv_in_chunks(temp_file, chunk_size=2)):
            print(f"  Chunk {i + 1}: {len(chunk)} rows")

        print("\n2. Testing data transformation:")
        raw_gen = read_csv_in_chunks(temp_file, chunk_size=10)
        for record in transform_data(raw_gen):
            print(f"  Transformed: {record}")

        print("\n3. Testing record filtering:")
        raw_gen = read_csv_in_chunks(temp_file, chunk_size=10)
        transformed_gen = transform_data(raw_gen)
        valid_count = 0
        for record in filter_valid_records(transformed_gen):
            valid_count += 1
            print(f"  Valid record: {record}")
        print(f"  Total valid records: {valid_count}")

        print("\n4. Testing paginated API iterator:")
        api_iter = PaginatedAPIIterator(total_items=25, page_size=10)
        for page in api_iter:
            print(f"  Page {page['page']}: {len(page['data'])} items, has_more: {page['has_more']}")

        print("\n5. Testing complete ETL pipeline:")
        for record in build_etl_pipeline(temp_file):
            print(f"  Clean record: {record}")
    
    finally:
        os.unlink(temp_file)


if __name__ == "__main__":
    main()
