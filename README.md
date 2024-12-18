# Web Scraping and MongoDB Integration

This project demonstrates how to scrape book data from the website `atticbooks.co.ke` using the Scrapy framework and store the extracted information in MongoDB. The project incorporates an ETL (Extract, Transform, Load) pipeline to process and manage the scraped data efficiently.

## Features:
- Scrape book title, price, and URL from product pages.
- Handle pagination to scrape data from multiple pages.
- Store the scraped data in MongoDB for easy retrieval.
- Integrate Scrapy with MongoDB via a custom pipeline.

## Requirements:
- Python 3.x
- Scrapy
- MongoDB
- pymongo library

## Installation:

### Step 1: Set up a Virtual Environment
```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:
```bash
.\venv\Scripts\Activate
```

For macOS/Linux:
```bash
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
python -m pip install scrapy pymongo
```

### Step 3: Set Up MongoDB
Ensure that MongoDB is installed and running on your machine. You can use `mongosh` to connect to MongoDB and create a database and collection:
```bash
mongosh
use books_db
db.createCollection("books")
```

### Step 4: Set Up Scrapy Project
```bash
scrapy startproject books
cd books
```

### Step 5: Create a Spider
Create a new spider to scrape data from `atticbooks.co.ke`:
```bash
scrapy genspider book https://atticbooks.co.ke/category/non-fiction-books
```

### Step 6: Configure the Spider
In `books/spiders/book.py`, modify the spider to extract book data (title, price, URL) and handle pagination.

### Step 7: Configure MongoDB Pipeline
In `books/pipelines.py`, set up a pipeline to insert scraped data into MongoDB. Modify the settings to point to your MongoDB URI and database.

### Step 8: Add the Pipeline to Settings
In `books/settings.py`, add the following to configure the pipeline:

```python
ITEM_PIPELINES = {
    "books.pipelines.BooksPipeline": 300,
}
MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "books_db"
```

### Step 9: Run the Spider
Run the spider to start scraping and storing the data in MongoDB:

```bash
scrapy crawl book
```

## How It Works:
1. **Scrapy Spider**: The spider scrapes the book details (title, price, URL) from each product page and follows pagination links to gather data from subsequent pages.
2. **MongoDB Pipeline**: The data scraped from the site is processed by the custom pipeline and stored in MongoDB, allowing easy access and manipulation.

## Project Structure:
```
books/
├── books/
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   ├── spiders/
│   │   └── book.py
├── scrapy.cfg
└── venv/
```

## Conclusion:
This project is a practical demonstration of web scraping, data processing, and database integration. It highlights the ability to automate data collection, structure it efficiently, and store it for future analysis using MongoDB.
