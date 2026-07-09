"""
Day 2: Decorators & Closures
Project: Build a Performance Monitoring System

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand function decorators and how they modify function behavior
- Learn about closures and how they capture variables from outer scope
- Implement decorator factories (decorators that accept parameters)
- Use functools.wraps to preserve function metadata
- Apply multiple decorators to a single function
- Understand decorator execution order (bottom to top)

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a comprehensive performance monitoring system that can:
1. Measure execution time of functions
2. Log function calls with parameters and return values
3. Cache expensive computations with time-to-live (TTL)
4. Automatically retry failed operations (e.g., API calls)
5. Combine multiple decorators for powerful function enhancement

=============================================================================
DECORATOR CONCEPTS:
=============================================================================
A decorator is a function that takes another function as input and returns
a new function that usually extends or modifies the original function's behavior.

Basic decorator structure:
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Do something before
            result = func(*args, **kwargs)
            # Do something after
            return result
        return wrapper

Decorator factory (accepts parameters):
    def decorator_factory(param):
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Use param
                result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. timer(func: Callable) -> Callable
   - Create a decorator that measures and prints execution time
   - Use time.time() before and after function call
   - Print the function name and execution time in seconds
   - Use @functools.wraps(func) to preserve function metadata
   - Example output: "[TIMER] process_data executed in 0.1234s"

2. logger(func: Callable) -> Callable
   - Create a decorator that logs function calls
   - Log the function name, arguments (*args), and keyword arguments (**kwargs)
   - Log the return value after the function completes
   - Use @functools.wraps(func) to preserve function metadata
   - Example output:
     "[LOGGER] Calling process_data with args=([1, 2, 3],), kwargs={}"
     "[LOGGER] process_data returned: [2, 4, 6]"

3. cache(ttl_seconds: int = 60)
   - Create a DECORATOR FACTORY that accepts TTL parameter
   - Cache function results in a dictionary
   - Each cache entry should store: (result, timestamp)
   - Check if cached result exists and is not expired
   - If expired or not cached, compute and store new result
   - Print cache hit/miss messages
   - Use datetime to track expiration
   - Example output:
     "[CACHE] Cached result for expensive_computation"
     "[CACHE] Cache hit for expensive_computation"

4. retry(max_attempts: int = 3, delay: float = 1.0)
   - Create a DECORATOR FACTORY that accepts max_attempts and delay
   - Try to execute the function up to max_attempts times
   - If function raises an exception, wait 'delay' seconds and retry
   - Print attempt number before each try
   - If all attempts fail, re-raise the last exception
   - Example output:
     "[RETRY] Attempt 1/3 for fetch_api_data"
     "[RETRY] Failed, retrying in 1.0s..."
     "[RETRY] Attempt 2/3 for fetch_api_data"

=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests all decorators:
1. process_data() - Tests @timer and @logger together
2. expensive_computation() - Tests @cache (first call slow, second fast)
3. fetch_api_data() - Tests @retry (random 70% success rate)
4. Cache expiration test - Waits 6 seconds to test TTL

Expected behavior:
- First call to expensive_computation takes ~0.5s
- Second call (cached) takes ~0.0s
- After 6 seconds, cache expires and third call takes ~0.5s again
- API call may fail and retry multiple times before success

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Add a @rate_limit decorator to limit function calls per second
- Add a @validate decorator to validate function arguments
- Add a @memoize decorator (cache without expiration)
- Add a @synchronize decorator for thread-safe function execution
- Create a decorator that measures memory usage
- Create a decorator that converts exceptions to return values
"""

import time
import functools
from datetime import datetime, timedelta
from typing import Callable, Any, Dict
import random


# =============================================================================
# KEY DECORATOR CONCEPTS - SIMPLE DECORATORS vs DECORATOR FACTORIES
# =============================================================================
# SIMPLE DECORATOR (e.g., @logger, @timer):
#   - Takes ONLY func as parameter
#   - Used as: @logger (no parentheses)
#   - Structure: def decorator(func) -> returns wrapper
#   - Python automatically passes the decorated function
#
# DECORATOR FACTORY (e.g., @cache, @retry):
#   - Takes parameters (ttl_seconds, max_attempts, etc.) - NOT func
#   - Used as: @cache(ttl_seconds=5) (WITH parentheses and params)
#   - Three-level structure:
#     1. Factory function: def cache(ttl_seconds=60) -> returns decorator
#     2. Decorator function: def decorator(func) -> returns wrapper
#     3. Wrapper function: def wrapper(*args, **kwargs) -> does work & returns result
#   - WRONG: def cache(ttl_seconds=60, func) - func should NOT be at factory level
#   - RIGHT: def cache(ttl_seconds=60): def decorator(func): def wrapper(...)
#
# EXECUTION FLOW for @cache(ttl_seconds=5):
#   1. cache(ttl_seconds=5) is called → returns a decorator function
#   2. @decorator is applied to expensive_computation → returns wrapper function
#   3. expensive_computation now points to wrapper
#
# WHY USE @functools.wraps(func)?
#   - Preserves original function's metadata: __name__, __doc__, __module__, __annotations__
#   - Without it: func.__name__ returns "wrapper" instead of actual function name
#   - Better debugging: Stack traces show real function names, not "wrapper"
#   - Essential for: documentation generators, introspection tools, debugging
#   - ALWAYS include it in every decorator's wrapper function
#   - Usage: @functools.wraps(func) decorator on the wrapper function
# =============================================================================


def timer(func: Callable) -> Callable:
    """
    Decorator that measures and prints the execution time of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] {func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """
    Decorator that logs function calls with parameters and return values.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] {func.__name__} returned: {result}")
        return result
    return wrapper


def cache(ttl_seconds: int = 60):
    """
    Decorator factory that caches function results with TTL (Time To Live).
    Results expire after ttl_seconds.
    """
    def decorator(func: Callable) -> Callable:
        cached_results: Dict[Any, tuple] = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (*args, frozenset(kwargs.items()))
            result = None
            if key in cached_results :
                result, timestamp = cached_results[key]
                timediff = datetime.now() - timestamp 
                print(f"timedifference : {timediff}")
                if(timediff < timedelta(seconds=ttl_seconds) ):
                    print(f"[CACHE] Cached result for {func.__name__} with Key {key}")
                    return result
                
                    
            
            result = func(*args, **kwargs)
            cached_results[key] = (result, datetime.now())
            return result
        
        return wrapper
    return decorator


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator that retries a function on failure.
    Simulates API call failures with random success rate.
    """
    def decorator(func: Callable) -> Callable:
       
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_attempts):
                try :

                    print(f"[Retry] attempt No {attempt+1}/{max_attempts} for function {__name__}")
                    return func(*args, **kwargs)
      
                except Exception as e :
                    last_error = e
                    print(f"[Retry] attempt No {attempt+1}/{max_attempts} for function {__name__} threw error {last_error}")
                    
                    if attempt < max_attempts -1:
                        print(f"[RETRY] Failed, retrying in {delay}s...")
                        time.sleep(delay)

            print(f"[RETRY] All {max_attempts} attempts failed for {func.__name__}")
            

        return wrapper
    
    return decorator


# Sample data processing functions to decorate
@timer
@logger
def process_data(data: list) -> list:
    """Process a list of data (simulated work)."""
    time.sleep(0.1)  # Simulate processing
    return [x * 2 for x in data]


@cache(ttl_seconds=6)
@logger
def expensive_computation(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(2)  # Simulate expensive operation
    return n ** 2


@retry(max_attempts=3, delay=0.5)
@logger
def fetch_api_data(endpoint: str) -> Dict:
    """Simulate fetching data from an API with random failures."""
    # 70% success rate
    if random.random() < 0.7:
        return {"status": "success", "data": [1, 2, 3, 4, 5]}
    raise ConnectionError("API request failed")


def main():
    print("=== Performance Monitoring System ===\n")

    # Test timer and logger
    print("1. Testing @timer and @logger:")
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Result: {result}\n")

    # Test cache
    print("2. Testing @cache (should be faster on second call):")
    start = time.time()
    expensive_computation(14)
    first_call = time.time() - start
    print(f"First call took: {first_call:.2f}s")

    start = time.time()
    expensive_computation(11)
    second_call = time.time() - start
    print(f"Second call (cached) took: {second_call:.2f}s\n")


    start = time.time()
    expensive_computation(14)
    third_call = time.time() - start
    print(f"Third call (cached) took: {third_call:.2f}s\n")


    # Test retry
    print("3. Testing @retry:")
    try:
        api_data = fetch_api_data("/api/users")
        print(f"API call succeeded: {api_data}\n")
    except Exception as e:
        print(f"API call failed after retries: {e}\n")

    # Test cache expiration
    print("4. Testing cache expiration (wait 6 seconds):")
    time.sleep(6)
    start = time.time()
    expensive_computation(10)
    third_call = time.time() - start
    print(f"Third call (cache expired) took: {third_call:.2f}s")


if __name__ == "__main__":
    main()
