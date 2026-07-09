"""
Day 3: Generators & Iterators
Project: Build a Streaming Data Pipeline

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand generators and the 'yield' keyword
- Learn how generators differ from lists (lazy evaluation)
- Implement custom iterators using __iter__ and __next__
- Chain generators together for data processing pipelines
- Understand memory efficiency of generators for large datasets
- Use generator expressions for concise code

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a streaming data pipeline (ETL - Extract, Transform, Load) that:
1. Reads large CSV files in chunks (memory-efficient)
2. Transforms data on-the-fly (type conversion, cleaning)
3. Filters out invalid records
4. Implements a custom iterator for paginated API responses
5. Chains all generators together for a complete pipeline

=============================================================================
GENERATOR CONCEPTS:
=============================================================================
A generator is a special type of function that returns an iterator.
Instead of returning all values at once (like a list), it yields one value
at a time, making it memory-efficient for large datasets.

Generator function:
    def my_generator():
        yield 1
        yield 2
        yield 3

Generator expression (like list comprehension but lazy):
    squares = (x**2 for x in range(1000000))  # Uses no memory until iterated

Iterator protocol:
    - __iter__(): Returns the iterator object
    - __next__(): Returns the next value, raises StopIteration when done



=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests all components:
1. Chunked CSV reading - Shows data in chunks
2. Data transformation - Shows converted types
3. Record filtering - Shows only valid records
4. Paginated iterator - Shows page-by-page fetching
5. Complete pipeline - Shows end-to-end ETL

Expected behavior:
- CSV is read in chunks of 2 rows
- String numbers are converted to integers
- Invalid records (missing id or name) are filtered out
- API iterator returns pages with 10 items each
- Pipeline yields clean, transformed records

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add a generator to deduplicate records
- Add a generator to aggregate data (e.g., sum by category)
- Implement async generators for concurrent processing
- Add error handling in the pipeline (skip bad rows, log errors)
- Create a generator that yields progress updates
- Implement backpressure handling for slow consumers
"""

from typing import Generator, Iterator, List, Dict, Any
import csv
from io import StringIO

'''
=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. read_csv_in_chunks(file_path: str, chunk_size: int = 1000)
   - Create a GENERATOR that reads CSV files in chunks
   - Use csv.DictReader to parse each row as a dictionary
   - Yield chunks (lists) of rows instead of all rows at once
   - This is crucial for processing files larger than memory
   - Hint: Use 'yield chunk' after accumulating chunk_size rows
   - Don't forget to yield the remaining rows after the loop

'''




def read_csv_in_chunks(file_path: str, chunk_size: int = 100) -> Generator[List[Dict[str, str]], None, None]:
    """
    Generator that reads a large CSV file in chunks.
    Yields lists of dictionaries representing rows.
    """
    # TODO: Implement chunked CSV reading
    
    with open(file_path, 'r') as f:
        # csv.dictreader itself is an lazy iterator or generator. AI please elaborate whats happening here
        read_data = csv.DictReader(f) 
        chunk = []
        for row in read_data :
            chunk.append(row)
            if len(chunk) >=chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

# filelocation = 'SampleData/day3_sample_data_large.csv'

# lazyreader = read_csv_in_chunks(filelocation, chunk_size=100)


# lazyreader.__next__()



'''
2. transform_data(data: Generator[List[Dict[str, str]], None, None])
   - Create a GENERATOR that transforms data on-the-fly
   - Input is a generator of chunks (lists of dictionaries)
   - For each row in each chunk:
     * Strip whitespace from string values
     * Convert numeric strings to integers
     * Yield individual transformed records (not chunks)
   - Hint: Use nested loops (for chunk in data: for row in chunk:)
'''


def transform_data(data: Generator[List[Dict[str, str]], None, None]) -> Generator[Dict[str, Any], None, None]:
    """
    Generator that transforms data on-the-fly.
    Converts string numbers to integers, cleans whitespace, etc.
    """
    # TODO: Implement data transformation
    
    for lazydata in data:
        
        for row in lazydata:
            transfirmed_data = {}
            for key, value in row.items():
                
                stripped_value = value.strip() if isinstance(value, str) else value
                    
                if stripped_value.isdigit() :
                    transfirmed_data[key] = int(stripped_value)
                else:
                    transfirmed_data[key] = stripped_value

            yield transfirmed_data
        




'''
3. filter_valid_records(data: Generator[Dict[str, Any], None, None])
   - Create a GENERATOR that filters invalid records
   - Check if required fields ('id', 'name') are present and non-empty
   - Only yield valid records
   - This is memory-efficient as it doesn't create a new list
   - Hint: Use 'if' condition before yielding

'''

def filter_valid_records(data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    """
    Generator that filters out invalid records.
    Records with missing required fields or invalid values are skipped.
    """
    # TODO: Implement record filtering
    for item in data:
        if 'id' in item and item["id"] and 'name' in item and item["name"] :
            yield item






'''
4. PaginatedAPIIterator (Custom Iterator Class)
   - Implement __iter__ method that returns self
   - Implement __next__ method that:
     * Raises StopIteration when all items are fetched
     * Simulates fetching a page of data
     * Returns a dict with: page number, data list, has_more flag
   - This demonstrates the iterator protocol for custom data sources
   - Hint: Track current_index and increment it in __next__

'''


class PaginatedAPIIterator:
    """
    Custom iterator for paginated API responses.
    Simulates fetching data page by page.
    """
    
    def __init__(self, total_items: int, page_size: int = 10):
        self.total_items = total_items
        self.page_size = page_size
        self.current_page = 0
        self.current_index = 0
    
    def __iter__(self):
        return self
    # AI please explain why you should not keepyeild inside next
    def __next__(self):
        
        
        data= {}
        if self.current_index >= self.total_items:
            raise StopIteration
        
        pagestart = self.current_index
        pageend = min(self.current_index + self.page_size, self.total_items)
        itemsinpage = list(range(pagestart, pageend))

        self.current_index = self.current_index + len(itemsinpage)
        self.current_page = self.current_page + 1

        data["page"] =  self.current_page
        data["data"] = itemsinpage
        data["has_more"] = self.current_index < self.total_items

        return data


'''
5. build_etl_pipeline(data_source: str)
   - Chain all generators together
   - Connect: read_csv_in_chunks -> transform_data -> filter_valid_records
   - This creates a complete ETL pipeline
   - Each generator processes data and passes it to the next
   - The pipeline is lazy - only processes when you iterate
   - Hint: Pass the output of one generator as input to the next

'''


def build_etl_pipeline(data_source: str) -> Generator[Dict[str, Any], None, None]:
    """
    Chain generators to build a complete ETL pipeline.
    Read -> Transform -> Filter -> Yield clean data
    """
    # TODO: Chain all generators together
    
    
    for item in filter_valid_records(transform_data(read_csv_in_chunks(data_source, chunk_size=10))):
        yield item


def main():
    print("=== Streaming Data Pipeline ===\n")

    from pathlib import Path

    test_data_path = Path(__file__).parent / 'SampleData' / 'day3_sample_data_large.csv'

    print("1. Testing chunked CSV reading:")
    for chunk_number, chunk in enumerate(read_csv_in_chunks(test_data_path, chunk_size=2), start=1):
        print(f"  Chunk {chunk_number}: {len(chunk)} rows")
        print(f"    First row in chunk: {chunk[0]}")
        if chunk_number >= 3:
            print("  ... stopping after 3 chunks for display")
            break

    print("\n2. Testing data transformation:")
    raw_data = read_csv_in_chunks(test_data_path, chunk_size=2)
    for record_number, record in enumerate(transform_data(raw_data), start=1):
        print(f"  Transformed record {record_number}: {record}")
        if record_number >= 5:
            print("  ... stopping after 5 records for display")
            break

    print("\n3. Testing record filtering:")
    sample_records = iter([
        {"id": 1, "name": "John", "age": 25},
        {"id": "", "name": "Missing Id", "age": 30},
        {"id": 2, "name": "", "age": 40},
        {"name": "Missing Id Key", "age": 50},
        {"id": 3, "name": "Jane", "age": 35},
    ])
    for record in filter_valid_records(sample_records):
        print(f"  Valid record: {record}")

    print("\n4. Testing paginated API iterator:")
    api_iterator = PaginatedAPIIterator(total_items=25, page_size=10)
    for page in api_iterator:
        # print(f"  Page {page['page']}: {len(page['data'])} items, has_more: {page['has_more']}")
        print(page)

    print("\n5. Testing complete ETL pipeline:")
    for record_number, record in enumerate(build_etl_pipeline(test_data_path), start=1):
        print(f"  Pipeline record {record_number}: {record}")
        if record_number >= 5:
            print("  ... stopping after 5 records for display")
            break

if __name__ == "__main__":
    main()
