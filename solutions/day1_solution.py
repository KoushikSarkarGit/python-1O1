"""
Day 1: Advanced Data Structures & Comprehensions
Project: Build a Log Analyzer System - SOLUTION
"""

from collections import Counter, defaultdict, OrderedDict
from datetime import datetime
import re
from typing import List, Dict, Tuple, Generator


def parse_log_line(line: str) -> Dict[str, str]:
    """Parse a single log line and extract timestamp, level, and message."""
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
    """Parse all log lines using list comprehension."""
    return [parse_log_line(line) for line in logs if parse_log_line(line)]


def count_error_types(logs: List[Dict[str, str]]) -> Counter:
    """Count the frequency of each log level using Counter."""
    return Counter(log['level'] for log in logs)


def group_logs_by_hour(logs: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Group logs by hour using defaultdict."""
    grouped = defaultdict(list)
    for log in logs:
        hour = log['timestamp'].split()[1].split(':')[0]
        grouped[hour].append(log.items())
    return dict(grouped)


def maintain_log_sequence(logs: List[Dict[str, str]]) -> OrderedDict:
    """Maintain the order of logs using OrderedDict."""
    ordered = OrderedDict()
    for log in logs:
        ordered[log['timestamp']] = log
    return ordered


def generate_statistics(logs: List[Dict[str, str]]) -> Generator[str, None, None]:
    """Generate statistics reports using generator expressions."""
    yield f"Total logs: {len(logs)}"
    yield f"ERROR count: {sum(1 for log in logs if log['level'] == 'ERROR')}"
    yield f"WARNING count: {sum(1 for log in logs if log['level'] == 'WARNING')}"
    yield f"INFO count: {sum(1 for log in logs if log['level'] == 'INFO')}"


def main():
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

    parsed_logs = parse_log_file(sample_logs)
    print(f"Parsed {len(parsed_logs)} log entries")

    error_counts = count_error_types(parsed_logs)
    print(f"\nError Types: {dict(error_counts)}")

    grouped = group_logs_by_hour(parsed_logs)
    print(f"\nLogs grouped by hour: {list(grouped.keys())}")

    ordered = maintain_log_sequence(parsed_logs)
    print(f"\nOrdered logs: {len(ordered)} entries")

    print("\nStatistics:")
    for stat in generate_statistics(parsed_logs):
        print(f"  {stat}")


if __name__ == "__main__":
    main()
