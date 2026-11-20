# Books Web Scraper

A Python script that scrapes book titles and prices from all 50 pages of [books.toscrape.com](https://books.toscrape.com) and saves them to a CSV file.

## What it does
- Visits all 50 catalogue pages automatically
- Extracts the title and price of every book (1000 books in total)
- Saves the data to `books.csv`, ready to open in Excel

## Tech used
- Python 3
- requests
- BeautifulSoup4
- csv

## How to run
1. Install the libraries:
   ```
   pip install requests beautifulsoup4
   ```
2. Run the script:
   ```
   python main.py
   ```
3. Open `books.csv` to see the results.

## Notes
- A short delay between requests keeps the scraper polite to the server.
- books.toscrape.com is a practice site built for learning web scraping.

## Author
Mariam Batool - BBIT student learning Python
