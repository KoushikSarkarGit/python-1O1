"""
Day 6: Async/Await & Concurrency
Project: Build an Async Web Scraper & API Client

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Understand async/await syntax and the event loop
- Learn how async functions differ from synchronous functions
- Implement async context managers and iterators
- Use asyncio for concurrent operations
- Implement rate limiting with semaphores
- Build async HTTP clients with connection pooling

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build an async web scraper that:
1. Fetches data from multiple websites concurrently
2. Uses async context managers for session management
3. Implements rate limiting to avoid overwhelming servers
4. Uses async iterators for paginated responses
5. Handles errors gracefully with retries

=============================================================================
ASYNC CONCEPTS:
=============================================================================
Async functions use 'async def' and 'await' keywords:
- async def: Defines a coroutine function
- await: Pauses execution until the awaited coroutine completes

Event loop: The scheduler that runs async tasks concurrently

Async context managers:
    async with AsyncSession() as session:
        result = await session.get(url)

Async iterators:
    async for item in async_iterator:
        process(item)

Semaphores: Limit concurrent operations
    semaphore = asyncio.Semaphore(10)  # Max 10 concurrent

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. fetch_url(session, url, semaphore)
   - Async function to fetch a single URL
   - Use semaphore to limit concurrent requests
   - Handle exceptions with try/except
   - Return (url, status, content) tuple
   - Use aiohttp or requests with async

2. fetch_all_urls(urls, max_concurrent=5)
   - Fetch multiple URLs concurrently
   - Create semaphore with max_concurrent limit
   - Create tasks for each URL
   - Use asyncio.gather to run tasks concurrently
   - Return list of results

3. AsyncSession (Async Context Manager)
   - Implement __aenter__ to create session
   - Implement __aexit__ to close session
   - Return session in __aenter__
   - Use aiohttp.ClientSession

4. PaginatedAPI (Async Iterator)
   - Implement __aiter__ to return self
   - Implement __anext__ to fetch next page
   - Raise StopAsyncIteration when done
   - Yield pages one at a time

5. scrape_websites(urls)
   - Use all async components together
   - Fetch data from multiple sites
   - Process results concurrently
   - Handle errors and retries

=============================================================================
TESTING YOUR CODE:
=============================================================================
The main() function tests all async components:
1. fetch_url - Single URL fetch with rate limiting
2. fetch_all_urls - Multiple concurrent fetches
3. AsyncSession - Session management
4. PaginatedAPI - Async iteration over pages
5. scrape_websites - Complete scraping pipeline

Expected behavior:
- Multiple URLs fetched concurrently (faster than sequential)
- Rate limiting prevents overwhelming servers
- Sessions are properly closed
- Pages are fetched one at a time via async iteration
- Errors are handled gracefully

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Implement async file I/O for saving results
- Add progress reporting during scraping
- Implement async queue for task distribution
- Add caching with async TTL
- Implement async websockets for real-time data
- Add timeout handling for requests
"""

import asyncio
from typing import List, Tuple, AsyncIterator, Dict, Any
from dataclasses import dataclass


@dataclass
class ScrapedData:
    url: str
    status: int
    content: str
    error: str = None


async def fetch_url(session, url: str, semaphore: asyncio.Semaphore) -> ScrapedData:
    """
    Async function to fetch a single URL with rate limiting.
    """
    # TODO: Implement async URL fetch with semaphore
    pass


async def fetch_all_urls(urls: List[str], max_concurrent: int = 5) -> List[ScrapedData]:
    """
    Fetch multiple URLs concurrently with rate limiting.
    """
    # TODO: Implement concurrent fetching with semaphore
    pass


class AsyncSession:
    """Async context manager for HTTP sessions."""
    
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        # TODO: Create and return async session
        pass
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # TODO: Close the session
        pass


class PaginatedAPI:
    """Async iterator for paginated API responses."""
    
    def __init__(self, base_url: str, total_pages: int = 5):
        self.base_url = base_url
        self.total_pages = total_pages
        self.current_page = 0
    
    def __aiter__(self) -> AsyncIterator[Dict[str, Any]]:
        # TODO: Return self as async iterator
        pass
    
    async def __anext__(self) -> Dict[str, Any]:
        # TODO: Fetch next page, raise StopAsyncIteration when done
        pass


async def scrape_websites(urls: List[str]) -> List[ScrapedData]:
    """
    Complete scraping pipeline using all async components.
    """
    # TODO: Implement complete scraping pipeline
    pass


async def main():
    print("=== Async Web Scraper ===\n")

    # Test fetch_url
    print("1. Testing fetch_url:")
    semaphore = asyncio.Semaphore(2)
    # result = await fetch_url(None, "https://httpbin.org/get", semaphore)
    # print(f"  Result: {result.status}\n")

    # Test fetch_all_urls
    print("2. Testing fetch_all_urls:")
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/uuid"
    ]
    # results = await fetch_all_urls(urls, max_concurrent=2)
    # print(f"  Fetched {len(results)} URLs\n")

    # Test AsyncSession
    print("3. Testing AsyncSession:")
    # async with AsyncSession() as session:
    #     print("  Session opened")
    # print("  Session closed\n")

    # Test PaginatedAPI
    print("4. Testing PaginatedAPI:")
    # api = PaginatedAPI("https://api.example.com/data", total_pages=3)
    # async for page in api:
    #     print(f"  Page {page['page']}")
    # print("  All pages fetched\n")

    # Test complete scraping
    print("5. Testing complete scraping:")
    # results = await scrape_websites(urls)
    # print(f"  Scraped {len(results)} websites")


if __name__ == "__main__":
    asyncio.run(main())
