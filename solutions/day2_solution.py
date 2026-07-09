"""
Day 2: Decorators & Closures
Project: Build a Performance Monitoring System - SOLUTION
"""

import time
import functools
from datetime import datetime, timedelta
from typing import Callable, Any, Dict
import random


def timer(func: Callable) -> Callable:
    """Decorator that measures and prints the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] {func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """Decorator that logs function calls with parameters and return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] {func.__name__} returned: {result}")
        return result
    return wrapper


def cache(ttl_seconds: int = 60):
    """Decorator factory that caches function results with TTL."""
    def decorator(func: Callable) -> Callable:
        cache_dict: Dict[Any, tuple] = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a cache key from args and kwargs
            key = (args, frozenset(kwargs.items()))
            
            # Check if result is cached and not expired
            if key in cache_dict:
                result, timestamp = cache_dict[key]
                if datetime.now() - timestamp < timedelta(seconds=ttl_seconds):
                    print(f"[CACHE] Cache hit for {func.__name__}")
                    return result
            
            # Compute and cache the result
            result = func(*args, **kwargs)
            cache_dict[key] = (result, datetime.now())
            print(f"[CACHE] Cached result for {func.__name__}")
            return result
        
        return wrapper
    return decorator


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator that retries a function on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    print(f"[RETRY] Attempt {attempt + 1}/{max_attempts} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"[RETRY] Failed, retrying in {delay}s...")
                        time.sleep(delay)
            print(f"[RETRY] All {max_attempts} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator


@timer
@logger
def process_data(data: list) -> list:
    """Process a list of data (simulated work)."""
    time.sleep(0.1)
    return [x * 2 for x in data]


@cache(ttl_seconds=5)
@logger
def expensive_computation(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.5)
    return n ** 2


@retry(max_attempts=3, delay=0.5)
@logger
def fetch_api_data(endpoint: str) -> Dict:
    """Simulate fetching data from an API with random failures."""
    if random.random() < 0.7:
        return {"status": "success", "data": [1, 2, 3, 4, 5]}
    raise ConnectionError("API request failed")


def main():
    print("=== Performance Monitoring System ===\n")

    print("1. Testing @timer and @logger:")
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Result: {result}\n")

    print("2. Testing @cache (should be faster on second call):")
    start = time.time()
    expensive_computation(10)
    first_call = time.time() - start
    print(f"First call took: {first_call:.2f}s")

    start = time.time()
    expensive_computation(10)
    second_call = time.time() - start
    print(f"Second call (cached) took: {second_call:.2f}s\n")

    print("3. Testing @retry:")
    try:
        api_data = fetch_api_data("/api/users")
        print(f"API call succeeded: {api_data}\n")
    except Exception as e:
        print(f"API call failed after retries: {e}\n")

    print("4. Testing cache expiration (wait 6 seconds):")
    time.sleep(6)
    start = time.time()
    expensive_computation(10)
    third_call = time.time() - start
    print(f"Third call (cache expired) took: {third_call:.2f}s")


if __name__ == "__main__":
    main()
