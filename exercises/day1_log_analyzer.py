"""
Day 1: Advanced Data Structures & Comprehensions
Project: Build a Log Analyzer System

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Master list comprehensions for data transformation
- Understand and use Counter for frequency counting
- Apply defaultdict for grouping data efficiently
- Use OrderedDict to maintain insertion order
- Implement generator expressions for memory-efficient processing

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a comprehensive log analyzer that processes server logs to extract
meaningful insights. The system should parse log files, count error types,
group logs by time periods, maintain chronological order, and generate
statistics reports efficiently.

=============================================================================
LOG FORMAT:
=============================================================================
Each log line follows this format:
    [YYYY-MM-DD HH:MM:SS] LEVEL: Message

Examples:
    [2024-01-15 10:30:45] ERROR: Database connection failed
    [2024-01-15 10:31:12] INFO: User logged in
    [2024-01-15 10:32:00] WARNING: High memory usage

Log Levels: ERROR, WARNING, INFO, DEBUG, CRITICAL

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. parse_log_file(logs: List[str]) -> List[Dict[str, str]]
   - Use LIST COMPREHENSION to parse all log lines
   - Filter out empty lines and invalid entries
   - Return a list of dictionaries with keys: timestamp, level, message
   - Hint: Use the parse_log_line function for each line

2. count_error_types(logs: List[Dict[str, str]]) -> Counter
   - Use Counter from collections module
   - Count the frequency of each log level (ERROR, INFO, WARNING, etc.)
   - Return a Counter object with the counts
   - Hint: Use a generator expression with Counter()

3. group_logs_by_hour(logs: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]
   - Use defaultdict from collections module
   - Extract the hour from each log's timestamp (e.g., "10" from "10:30:45")
   - Group all logs that occurred in the same hour
   - Return a dictionary where keys are hours and values are lists of logs
   - Hint: defaultdict(list) automatically creates empty lists for new keys

4. maintain_log_sequence(logs: List[Dict[str, str]]) -> OrderedDict
   - Use OrderedDict from collections module
   - Use the timestamp as the key to ensure logs stay in chronological order
   - OrderedDict remembers the order in which items were inserted
   - Return an OrderedDict with timestamps as keys and log dicts as values
   - Hint: Sort logs by timestamp before adding to OrderedDict

5. generate_statistics(logs: List[Dict[str, str]])
   - Use GENERATOR EXPRESSION to yield statistics one at a time
   - This is memory-efficient for large datasets
   - Yield the following statistics in order:
     * Total number of logs
     * Count of ERROR logs
     * Count of WARNING logs
     * Count of INFO logs
   - Hint: Use "yield" instead of "return" to create a generator

=============================================================================
TESTING YOUR CODE:
=============================================================================
Run the main() function to test your implementation with sample data.
Expected output:
- Parsed 8 log entries
- Error Types: {'ERROR': 3, 'INFO': 3, 'WARNING': 2}
- Logs grouped by hour: ['10']
- Ordered logs: 8 entries
- Statistics showing counts for each level

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add a function to filter logs by level using list comprehension
- Add a function to find the most common error message using Counter
- Add a function to calculate time differences between consecutive logs
- Add a function to detect patterns (e.g., repeated errors within 1 minute)
"""

from collections import Counter, defaultdict, OrderedDict
from datetime import datetime
import re
from typing import List, Dict, Tuple


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parse a single log line and extract timestamp, level, and message.
    Use regex and dictionary comprehension.
    """
    pattern = r'\[(.*?)\] (\w+): (.*)'
    match = re.match(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return {}


def parse_log_file(logs: List[str]) -> List[Dict[str, str]]:
    """
    Parse all log lines using list comprehension.
    Filter out empty lines and invalid entries.
    """
    # TODO: Implement using list comprehension 
    loglist = [ parse_log_line(item)  for item in logs if parse_log_line(item)]
    return loglist


def count_error_types(logs: List[Dict[str, str]]) -> Counter:
    """
    Count the frequency of each log level using Counter.
    """
    # TODO: Implement using Counter
    return Counter(item["level"] for item in logs)


def group_logs_by_hour(logs: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Group logs by hour using defaultdict.
    Extract hour from timestamp and group accordingly.
    """
    # TODO: Implement using defaultdict
    groupeddict = defaultdict(list)
    for item in logs :
        hour = item["timestamp"].split()[1].split(":")[0]
        groupeddict[hour].append(list(item.items()))
    return dict (groupeddict)


def maintain_log_sequence(logs: List[Dict[str, str]]) -> OrderedDict:
    """
    Maintain the order of logs using OrderedDict.
    Use timestamp as key to ensure chronological order.
    """
    # TODO: Implement using OrderedDict
    ordered = OrderedDict()
    for item in logs:
        ordered[item["timestamp"]] = item
    return ordered


def generate_statistics(logs: List[Dict[str, str]]):
    """
    Generate statistics reports using generator expressions.
    Yield statistics one at a time to be memory efficient.
    """
    # Yield: total logs, error count, warning count, info count
    yield len(logs)
    yield sum(1 for item in logs if item["level"] == "ERROR")
    yield sum(1 for item in logs if item["level"] == "WARNING")
    yield sum(1 for item in logs if item["level"] == "INFO")


def main():
    # Sample log data
    sample_logs = [
        "[2024-01-15 10:30:45] ERROR: Database connection failed",
        "[2024-01-15 10:31:12] INFO: User logged in",
        "[2024-01-15 10:32:00] WARNING: High memory usage",
        "[2024-01-15 10:33:15] ERROR: File not found",
        "[2024-01-15 10:34:30] INFO: Request processed",
        "[2024-01-15 10:35:45] WARNING: Disk space low",
        "[2024-01-15 10:36:00] ERROR: Timeout occurred",
        "[2024-01-15 10:37:15] INFO: Cache cleared",
    ]

    print("=== Log Analyzer System ===\n")

    # Parse logs
    parsed_logs = parse_log_file(sample_logs)
    print(f"Parsed {len(parsed_logs)} log entries")

    # Count error types
    error_counts = count_error_types(parsed_logs)
    print(f"\nError Types: {dict(error_counts)}")

    # Group by hour
    grouped = group_logs_by_hour(parsed_logs)
    print(f"\nLogs grouped by hour: {list(grouped.keys())}")
    print(grouped)
    for hour in grouped.keys():
        for item in grouped[hour]:
            print("for hour", hour, ":", item)

    # Maintain sequence
    ordered = maintain_log_sequence(parsed_logs)
    print(f"\nOrdered logs: {len(ordered)} entries")

    # Generate statistics
    print("\nStatistics:")
    for stat in generate_statistics(parsed_logs):
        print(f"  {stat}")


if __name__ == "__main__":
    main()
