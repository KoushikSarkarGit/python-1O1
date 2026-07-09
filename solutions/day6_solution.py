"""
Day 6: Async/Await & Concurrency
Project: Build an Async Web Scraper & API Client - SOLUTION
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
    """Async function to fetch a single URL with rate limiting."""
    async with semaphore:
        try:
            # Simulate async fetch (replace with actual aiohttp)
            await asyncio.sleep(0.1)
            return ScrapedData(url=url, status=200, content=f"Content from {url}")
        except Exception as e:
            return ScrapedData(url=url, status=500, content="", error=str(e))


async def fetch_all_urls(urls: List[str], max_concurrent: int = 5) -> List[ScrapedData]:
    """Fetch multiple URLs concurrently with rate limiting."""
    semaphore = asyncio.Semaphore(max_concurrent)
    # Simulate session (replace with actual aiohttp session)
    session = None
    tasks = [fetch_url(session, url, semaphore) for url in urls]
    return await asyncio.gather(*tasks)


class AsyncSession:
    """Async context manager for HTTP sessions."""
    
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        # Simulate session creation
        self.session = "mock_session"
        return self.session
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Simulate session close
        self.session = None


class PaginatedAPI:
    """Async iterator for paginated API responses."""
    
    def __init__(self, base_url: str, total_pages: int = 5):
        self.base_url = base_url
        self.total_pages = total_pages
        self.current_page = 0
    
    def __aiter__(self) -> AsyncIterator[Dict[str, Any]]:
        return self
    
    async def __anext__(self) -> Dict[str, Any]:
        if self.current_page >= self.total_pages:
            raise StopAsyncIteration
        self.current_page += 1
        await asyncio.sleep(0.1)  # Simulate API call
        return {
            'page': self.current_page,
            'data': list(range((self.current_page - 1) * 10, self.current_page * 10)),
            'has_more': self.current_page < self.total_pages
        }


async def scrape_websites(urls: List[str]) -> List[ScrapedData]:
    """Complete scraping pipeline using all async components."""
    async with AsyncSession() as session:
        semaphore = asyncio.Semaphore(3)
        tasks = [fetch_url(session, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)


async def main():
    print("=== Async Web Scraper ===\n")

    print("1. Testing fetch_all_urls:")
    urls = ["https://example.com/1", "https://example.com/2", "https://example.com/3"]
    results = await fetch_all_urls(urls, max_concurrent=2)
    print(f"  Fetched {len(results)} URLs")
    for result in results:
        print(f"    {result.url}: {result.status}\n")

    print("2. Testing AsyncSession:")
    async with AsyncSession() as session:
        print(f"  Session opened: {session is not None}")
    print("  Session closed\n")

    print("3. Testing PaginatedAPI:")
    api = PaginatedAPI("https://api.example.com/data", total_pages=3)
    async for page in api:
        print(f"  Page {page['page']}: {len(page['data'])} items")
    print("  All pages fetched\n")


if __name__ == "__main__":
    asyncio.run(main())
