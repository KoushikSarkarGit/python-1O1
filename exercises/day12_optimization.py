"""
Day 12: Performance Optimization & Profiling
Project: Optimize a Data Processing System

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Profile code with cProfile and line_profiler
- Identify performance bottlenecks
- Optimize database queries
- Implement caching strategies
- Use generators for memory efficiency
- Optimize algorithms (time complexity)
- Benchmark before/after performance

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Optimize a data processing system by:
1. Profiling existing code to find bottlenecks
2. Optimizing database queries
3. Implementing caching strategies
4. Using generators for memory efficiency
5. Optimizing algorithms
6. Benchmarking improvements

=============================================================================
PROFILING CONCEPTS:
=============================================================================
cProfile: Built-in Python profiler
    python -m cProfile -s time script.py

line_profiler: Line-by-line profiling
    @profile
    def my_function():
        pass

memory_profiler: Memory usage profiling
    python -m memory_profiler script.py

Time complexity: Algorithm efficiency
    O(1) - Constant
    O(n) - Linear
    O(n^2) - Quadratic
    O(log n) - Logarithmic

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. profile_function(func)
   - Use cProfile to profile a function
   - Print top 10 slowest functions
   - Identify bottlenecks
   - Return profiling stats

2. optimize_database_query(query)
   - Add indexes to columns
   - Use select only needed columns
   - Use joins efficiently
   - Implement query batching

3. implement_cache(func, ttl=3600)
   - Use functools.lru_cache
   - Or implement custom cache
   - Add TTL support
   - Cache expensive computations

4. use_generator_for_memory(data)
   - Convert list processing to generator
   - Process data in chunks
   - Reduce memory usage
   - Maintain same functionality

5. optimize_algorithm(data)
   - Improve time complexity
   - Use better data structures
   - Reduce nested loops
   - Use built-in functions

6. benchmark_before_after(func, data)
   - Measure time before optimization
   - Measure time after optimization
   - Calculate speedup
   - Print comparison

=============================================================================
TESTING YOUR CODE:
=============================================================================
Test optimizations:
1. Profile slow function
2. Optimize database query
3. Add caching
4. Convert to generator
5. Optimize algorithm
6. Benchmark improvements

Expected results:
- Identify bottlenecks
- Measure performance gains
- Reduce memory usage
- Improve time complexity

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Use multiprocessing for CPU-bound tasks
- Implement async I/O for network operations
- Use Cython for critical sections
- Implement connection pooling
- Add query result caching
- Use numpy for numerical operations
"""

import cProfile
import pstats
import time
import functools
from typing import Callable, List, Any, Generator
from io import StringIO


def profile_function(func: Callable, *args, **kwargs):
    """
    Profile a function and print results.
    """
    # TODO: Implement profiling with cProfile
    pass


def slow_function(n: int) -> int:
    """A slow function to optimize."""
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result


def optimized_function(n: int) -> int:
    """Optimized version using math."""
    # TODO: Implement optimized version
    pass


def process_data_list(data: List[int]) -> List[int]:
    """Process data using list (memory intensive)."""
    # TODO: Implement list-based processing
    pass


def process_data_generator(data: List[int]) -> Generator[int, None, None]:
    """Process data using generator (memory efficient)."""
    # TODO: Implement generator-based processing
    pass


def cache_decorator(ttl: int = 3600):
    """Decorator for caching function results."""
    # TODO: Implement caching with TTL
    pass


@cache_decorator(ttl=60)
def expensive_computation(n: int) -> int:
    """Expensive computation to cache."""
    time.sleep(0.1)
    return sum(range(n))


def benchmark(func: Callable, *args, **kwargs) -> float:
    """
    Benchmark a function and return execution time.
    """
    # TODO: Implement benchmarking
    pass


def optimize_database_query():
    """
    Example of database query optimization.
    """
    # TODO: Show before/after query optimization
    pass


def main():
    print("=== Performance Optimization ===\n")

    # Test profiling
    print("1. Profiling slow function:")
    profile_function(slow_function, 100)
    print()

    # Test optimization
    print("2. Benchmarking before/after optimization:")
    slow_time = benchmark(slow_function, 100)
    fast_time = benchmark(optimized_function, 100)
    print(f"  Slow: {slow_time:.4f}s")
    print(f"  Fast: {fast_time:.4f}s")
    print(f"  Speedup: {slow_time/fast_time:.2f}x\n")

    # Test caching
    print("3. Testing caching:")
    first = benchmark(expensive_computation, 1000)
    second = benchmark(expensive_computation, 1000)
    print(f"  First call: {first:.4f}s")
    print(f"  Second call (cached): {second:.4f}s\n")

    # Test generator vs list
    print("4. Testing memory efficiency:")
    data = list(range(100000))
    list_result = process_data_list(data[:100])
    gen_result = list(process_data_generator(data[:100]))
    print(f"  List result: {len(list_result)}")
    print(f"  Generator result: {len(gen_result)}\n")


if __name__ == "__main__":
    main()
