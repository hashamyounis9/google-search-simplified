# Google Search Scraper API

This is a Flask-based API that scrapes Google search results asynchronously using the `nodriver` package for browser automation and `BeautifulSoup` for HTML parsing. The API returns detailed information about search results, including URLs, titles, site names, and overviews.

## Features

- **Asynchronous Scraping:** Uses `asyncio` and `nodriver` to scrape Google search results efficiently.
- **Headless Browser Automation:** The API runs the browser in headless mode for fast and resource-efficient scraping.
- **HTML Parsing:** Utilizes `BeautifulSoup` to extract and organize data from the HTML content.
- **Customizable Queries:** Allows users to perform Google searches through a simple API endpoint.

## Prerequisites

Before running the API, ensure that you have the following installed:

- Python 3.7 or higher
- `nodriver` package
- `Flask` package
- `BeautifulSoup` package
- `asyncio` package

You can install the required packages using `pip`:

```bash
pip install flask nodriver beautifulsoup4 asyncio
