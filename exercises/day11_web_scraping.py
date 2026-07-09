"""
Day 11: Web Scraping & Automation
Project: Build a Product Price Monitor

=============================================================================
LEARNING OBJECTIVES:
=============================================================================
- Use requests and BeautifulSoup for web scraping
- Handle pagination and rate limiting
- Store scraped data in database
- Implement price change alerts
- Schedule periodic scraping
- Handle anti-scraping measures

=============================================================================
PROJECT OVERVIEW:
=============================================================================
Build a product price monitor that:
1. Scrapes product data from e-commerce sites
2. Handles pagination to get all products
3. Implements rate limiting to avoid blocking
4. Stores data in database
5. Detects price changes and sends alerts
6. Runs periodically to track prices over time

=============================================================================
WEB SCRAPING CONCEPTS:
=============================================================================
requests: HTTP library for making requests
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

BeautifulSoup: HTML/XML parsing library
    soup.find('div', class_='price')
    soup.find_all('a', href=True)

Rate limiting: Delay between requests
    time.sleep(1)  # Wait 1 second between requests

User agents: Identify your scraper
    headers = {'User-Agent': 'Mozilla/5.0...'}

=============================================================================
TASKS TO COMPLETE:
=============================================================================

1. fetch_page(url, headers)
   - Make HTTP request with requests
   - Handle connection errors
   - Return BeautifulSoup object
   - Implement retry logic

2. extract_product_data(soup)
   - Parse product name, price, availability
   - Handle missing data gracefully
   - Return dictionary with product info
   - Use CSS selectors

3. scrape_category(base_url, max_pages=5)
   - Handle pagination
   - Scrape multiple pages
   - Implement rate limiting
   - Return list of products

4. store_in_database(products)
   - Connect to database
   - Insert or update products
   - Track price history
   - Handle duplicates

5. detect_price_changes(new_products, old_products)
   - Compare current prices with previous
   - Identify price drops
   - Generate alerts
   - Return list of changes

6. send_alert(product, old_price, new_price)
   - Send email notification
   - Or log to file
   - Format alert message
   - Handle send errors

7. schedule_scraping(interval_hours=24)
   - Run scraping periodically
   - Use schedule library or time.sleep
   - Log each run
   - Handle errors gracefully

=============================================================================
TESTING YOUR CODE:
=============================================================================
Test scraping on a real website:
1. Scrape a single product page
2. Scrape a category with pagination
3. Store data in database
4. Run again to detect price changes
5. Test rate limiting
6. Test error handling

=============================================================================
ADVANCED CHALLENGES (Optional):
=============================================================================
- Use Scrapy framework for large-scale scraping
- Handle JavaScript-rendered pages with Selenium
- Add proxy rotation
- Implement distributed scraping
- Add CAPTCHA solving
- Scrape multiple e-commerce sites
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time
from datetime import datetime
import sqlite3


def fetch_page(url: str, headers: Dict[str, str] = None) -> Optional[BeautifulSoup]:
    """
    Fetch a web page and return BeautifulSoup object.
    """
    # TODO: Implement page fetching with error handling
    pass


def extract_product_data(soup: BeautifulSoup) -> Optional[Dict[str, any]]:
    """
    Extract product data from parsed HTML.
    """
    # TODO: Implement product data extraction
    pass


def scrape_category(base_url: str, max_pages: int = 5) -> List[Dict[str, any]]:
    """
    Scrape all products from a category with pagination.
    """
    # TODO: Implement pagination scraping with rate limiting
    pass


def store_in_database(products: List[Dict[str, any]], db_path: str = "products.db"):
    """
    Store scraped products in database.
    """
    # TODO: Implement database storage
    pass


def detect_price_changes(new_products: List[Dict], old_products: List[Dict]) -> List[Dict]:
    """
    Detect price changes between current and previous scrape.
    """
    # TODO: Implement price change detection
    pass


def send_alert(product: Dict, old_price: float, new_price: float):
    """
    Send alert for price change.
    """
    # TODO: Implement alert sending (email or log)
    pass


def schedule_scraping(base_url: str, interval_hours: int = 24):
    """
    Schedule periodic scraping.
    """
    # TODO: Implement scheduling
    pass


def main():
    print("=== Product Price Monitor ===\n")

    # Test single page fetch
    print("1. Testing page fetch:")
    # soup = fetch_page("https://example.com/product")
    # print(f"  Page fetched: {soup is not None}\n")

    # Test product extraction
    print("2. Testing product extraction:")
    # if soup:
    #     product = extract_product_data(soup)
    #     print(f"  Product: {product}\n")

    # Test category scraping
    print("3. Testing category scraping:")
    # products = scrape_category("https://example.com/category", max_pages=2)
    # print(f"  Scraped {len(products)} products\n")

    # Test database storage
    print("4. Testing database storage:")
    # store_in_database(products)
    # print("  Products stored\n")

    # Test price change detection
    print("5. Testing price change detection:")
    # changes = detect_price_changes(products, [])
    # print(f"  Price changes: {len(changes)}\n")


if __name__ == "__main__":
    main()
