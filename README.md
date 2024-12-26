# 📚 Web Scraping Project with Scrapy and MongoDB

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue) 
![Scrapy Version](https://img.shields.io/badge/scrapy-2.6.1-brightgreen) 
![MongoDB](https://img.shields.io/badge/mongodb-database-brightgreen)
![License](https://img.shields.io/github/license/AathifZahir/Py-Scrap) 
![Last Commit](https://img.shields.io/github/last-commit/AathifZahir/Py-Scrap) 

---

## 📋 Table of Contents

- [📖 About the Project](#about-the-project)
- [⚙️ Getting Started](#getting-started)
  - [📦 Prerequisites](#prerequisites)
  - [🔧 Setup Instructions](#setup-instructions)
- [💡 Running the Scraper](#running-the-scraper)
- [📂 Project Structure](#project-structure)
- [✨ Customization](#customization)
- [📜 License](#license)
- [📚 References](#references)

---

## 📖 About the Project

This project demonstrates how to build a web scraper using **Scrapy**, a powerful Python framework for web scraping, and store the extracted data in **MongoDB**, a flexible NoSQL database. 

### Objective

The scraper is designed to extract book information from **Amazon**. It:
- Extracts relevant data like book titles, prices, ratings, and images.
- Handles pagination to scrape data across multiple pages.
- Stores the extracted data in a MongoDB database for further analysis or processing.

---

## ⚙️ Getting Started

Follow these steps to get the project running on your local machine. 🚀

### 📦 Prerequisites

Before running the scraper, ensure you have the following installed:
- 🐍 Python 3.9 or higher
- 🕷️ Scrapy
- 💾 MongoDB
- 🔗 pymongo

---

### 🔧 Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/books_scraper.git
   cd books_scraper
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or macOS:

     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Packages**:

   ```bash
   pip install scrapy pymongo
   ```

5. **Configure MongoDB**:

   Ensure MongoDB is installed and running on your local machine. The default connection settings in the project are:
   - Host: `localhost`
   - Port: `27017`
   - Database: `books_db`
   - Collection: `books`

   If your MongoDB configuration differs, update the settings in `settings.py` accordingly.

---

## 💡 Running the Scraper

To execute the scraper, use the following command:

```bash
scrapy crawl book -a keyword="laptops"
```

The scraper will:
- Use the passed keyword (default is "books").
- Start at the specified Amazon search URL.
- Navigate through the pages and extract data like book titles, prices, ratings, and images.
- Store the extracted data in the MongoDB database.

If you do not pass a keyword, the scraper will default to searching for "books". Example:

```bash
scrapy crawl book
```

---

## 📂 Project Structure

The project follows Scrapy's standard structure:

```
books_scraper/
├── books/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── book_spider.py
├── scrapy.cfg
└── README.md
```

- `items.py`: Defines the data structure for the scraped items.
- `pipelines.py`: Contains the pipeline for processing and storing items in MongoDB.
- `settings.py`: Configuration settings for the Scrapy project, including MongoDB connection details.
- `spiders/book_spider.py`: The main spider responsible for scraping Amazon.

---

## ✨ Customization

To adapt the scraper for different keywords or websites:

1. **Pass a Keyword Dynamically**:

   The spider can be run with a dynamic keyword using the `-a` argument. Example for scraping books related to "laptops":

   ```bash
   scrapy crawl book -a keyword="laptops"
   ```

   By default, if no keyword is passed, the scraper will search for "books".

2. **Update the `start_urls`**:

   Modify the `start_urls` list in `book_spider.py` to point to a different website or category.

3. **Adjust the Parsing Logic**:

   Ensure the CSS selectors in the `parse` method of `book_spider.py` accurately target the desired data fields on the new website.

4. **Handle Pagination**:

   If the target website uses a different pagination structure, update the pagination handling logic in the `parse` method accordingly.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details. 📄

---

## 📚 References

For more detailed information on the tools and techniques used in this project, refer to the following resources:
- 📖 [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
- 🗃️ [Scrapy MongoDB Pipeline](https://github.com/julien-duponchelle/scrapy-mongodb)
- 📰 [Web Scraping With Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)

---

## ⭐ Support

If you like this project, please give it a ⭐ by clicking the star button at the top of the repository! It helps others discover the project and motivates me to improve it further. ❤️

---

This update now allows users to pass a custom keyword for the search and if not passed, the default is "books".
