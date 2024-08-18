# Google Search Simplified API

Google Search Simplified is an API that allows you to perform Google searches and retrieve search results in a structured JSON format. This API is built using Flask, asyncio, and uses a headless browser for scraping Google search results.

## Features

- **Asynchronous Scraping**: Efficiently scrape Google search results using asyncio.
- **Structured Output**: Returns search results including titles, URLs, site names, overviews, and site logos in JSON format.
- **Error Handling**: Provides clear error messages and hints for invalid or unclear queries.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. You will also need to install the required packages:

```bash
pip install Flask nodriver beautifulsoup4 asyncio