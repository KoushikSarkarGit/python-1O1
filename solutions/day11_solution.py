"""
Day 11: Web Scraping & Automation
Project: Build a Product Price Monitor - SOLUTION
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time
from datetime import datetime
import sqlite3


def fetch_page(url: str, headers: Dict[str, str] = None) -> Optional[BeautifulSoup]:
    """Fetch a web page and return BeautifulSoup object."""
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_product_data(soup: BeautifulSoup) -> Optional[Dict[str, any]]:
    """Extract product data from parsed HTML."""
    # This is a template - actual selectors depend on the website
    try:
        name = soup.find('h1', class_='product-name').text.strip()
        price = soup.find('span', class_='price').text.strip()
        availability = soup.find('span', class_='availability').text.strip()
        
        return {
            'name': name,
            'price': float(price.replace('$', '').replace(',', '')),
            'availability': availability,
            'scraped_at': datetime.utcnow().isoformat()
        }
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None


def scrape_category(base_url: str, max_pages: int = 5) -> List[Dict[str, any]]:
    """Scrape all products from a category with pagination."""
    all_products = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}: {url}")
        
        soup = fetch_page(url)
        if not soup:
            continue
        
        # Find all product links
        product_links = soup.find_all('a', class_='product-link')
        
        for link in product_links[:5]:  # Limit for demo
            product_url = link['href']
            product_soup = fetch_page(product_url)
            if product_soup:
                product = extract_product_data(product_soup)
                if product:
                    all_products.append(product)
        
        time.sleep(1)  # Rate limiting
    
    return all_products


def store_in_database(products: List[Dict[str, any]], db_path: str = "products.db"):
    """Store scraped products in database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            availability TEXT,
            scraped_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            price REAL,
            recorded_at TEXT
        )
    ''')
    
    for product in products:
        cursor.execute('''
            INSERT OR REPLACE INTO products (name, price, availability, scraped_at)
            VALUES (?, ?, ?, ?)
        ''', (product['name'], product['price'], product['availability'], product['scraped_at']))
        
        cursor.execute('''
            INSERT INTO price_history (product_name, price, recorded_at)
            VALUES (?, ?, ?)
        ''', (product['name'], product['price'], datetime.utcnow().isoformat()))
    
    conn.commit()
    conn.close()


def detect_price_changes(new_products: List[Dict], old_products: List[Dict]) -> List[Dict]:
    """Detect price changes between current and previous scrape."""
    changes = []
    old_dict = {p['name']: p['price'] for p in old_products}
    
    for new_product in new_products:
        name = new_product['name']
        new_price = new_product['price']
        
        if name in old_dict:
            old_price = old_dict[name]
            if new_price != old_price:
                changes.append({
                    'name': name,
                    'old_price': old_price,
                    'new_price': new_price,
                    'change': new_price - old_price,
                    'change_percent': ((new_price - old_price) / old_price) * 100
                })
    
    return changes


def send_alert(product: Dict, old_price: float, new_price: float):
    """Send alert for price change."""
    change = new_price - old_price
    change_type = "increased" if change > 0 else "decreased"
    
    message = f"""
    PRICE ALERT for {product['name']}:
    Old price: ${old_price:.2f}
    New price: ${new_price:.2f}
    Change: ${abs(change):.2f} ({change_type})
    """
    
    print(message)
    # In production, send email via SMTP or use a notification service


def schedule_scraping(base_url: str, interval_hours: int = 24):
    """Schedule periodic scraping."""
    while True:
        print(f"Starting scrape at {datetime.utcnow()}")
        products = scrape_category(base_url, max_pages=2)
        store_in_database(products)
        print(f"Scraped {len(products)} products")
        print(f"Next scrape in {interval_hours} hours")
        time.sleep(interval_hours * 3600)


def main():
    print("=== Product Price Monitor ===\n")

    # Simulate scraping (without actual website)
    print("1. Simulating page fetch:")
    # soup = fetch_page("https://example.com/product")
    print("   (Simulated - would fetch actual page)\n")

    print("2. Simulating product extraction:")
    sample_product = {
        'name': 'Sample Product',
        'price': 99.99,
        'availability': 'In Stock',
        'scraped_at': datetime.utcnow().isoformat()
    }
    print(f"   Product: {sample_product}\n")

    print("3. Simulating category scraping:")
    products = [sample_product] * 3
    print(f"   Scraped {len(products)} products\n")

    print("4. Testing database storage:")
    store_in_database(products)
    print("   Products stored\n")

    print("5. Testing price change detection:")
    old_products = [{'name': 'Sample Product', 'price': 99.99}]
    new_products = [{'name': 'Sample Product', 'price': 89.99}]
    changes = detect_price_changes(new_products, old_products)
    print(f"   Price changes: {len(changes)}")
    for change in changes:
        print(f"     {change}")


if __name__ == "__main__":
    main()
