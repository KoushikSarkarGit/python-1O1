"""
Day 12: Performance Optimization & Profiling
Project: Optimize a Data Processing System - SOLUTION
"""

import cProfile
import pstats
import time
import functools
from typing import Callable, List, Any, Generator
from io import StringIO


def profile_function(func: Callable, *args, **kwargs):
    """Profile a function and print results."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)
    
    return result


def slow_function(n: int) -> int:
    """A slow function to optimize."""
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result


def optimized_function(n: int) -> int:
    """Optimized version using math."""
    # Mathematical optimization: sum(i*j) for i,j in [0,n) = (sum(i))^2
    # sum(i) for i in [0,n) = n*(n-1)/2
    total = n * (n - 1) // 2
    return total * total


def process_data_list(data: List[int]) -> List[int]:
    """Process data using list (memory intensive)."""
    return [x * 2 for x in data if x % 2 == 0]


def process_data_generator(data: List[int]) -> Generator[int, None, None]:
    """Process data using generator (memory efficient)."""
    for x in data:
        if x % 2 == 0:
            yield x * 2


def cache_decorator(ttl: int = 3600):
    """Decorator for caching function results."""
    cache = {}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                cached_time, result = cache[key]
                if time.time() - cached_time < ttl:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (time.time(), result)
            return result
        return wrapper
    return decorator


@cache_decorator(ttl=60)
def expensive_computation(n: int) -> int:
    """Expensive computation to cache."""
    time.sleep(0.1)
    return sum(range(n))


def benchmark(func: Callable, *args, **kwargs) -> float:
    """Benchmark a function and return execution time."""
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return end - start


def optimize_database_query():
    """Example of database query optimization."""
    print("\n=== Database Query Optimization ===")
    print("Before: SELECT * FROM users")
    print("After: SELECT id, name FROM users WHERE active = 1")
    print("Benefits: Reduced data transfer, indexed column used")
    print("\nBefore: Iterate and update one by one")
    print("After: UPDATE users SET status = 'active' WHERE id IN (1,2,3)")
    print("Benefits: Single query instead of multiple queries")


def main():
    print("=== Performance Optimization ===\n")

    print("1. Profiling slow function:")
    profile_function(slow_function, 100)
    print()

    print("2. Benchmarking before/after optimization:")
    slow_time = benchmark(slow_function, 100)
    fast_time = benchmark(optimized_function, 100)
    print(f"   Slow: {slow_time:.4f}s")
    print(f"   Fast: {fast_time:.4f}s")
    print(f"   Speedup: {slow_time/fast_time:.2f}x\n")

    print("3. Testing caching:")
    first = benchmark(expensive_computation, 1000)
    second = benchmark(expensive_computation, 1000)
    print(f"   First call: {first:.4f}s")
    print(f"   Second call (cached): {second:.4f}s")
    print(f"   Speedup: {first/second:.2f}x\n")

    print("4. Testing memory efficiency:")
    data = list(range(100000))
    list_result = process_data_list(data[:100])
    gen_result = list(process_data_generator(data[:100]))
    print(f"   List result: {len(list_result)}")
    print(f"   Generator result: {len(gen_result)}")
    print("   Generator uses constant memory regardless of input size\n")

    optimize_database_query()


if __name__ == "__main__":
    main()
