# 📚 Web Scraping Project with Scrapy and MongoDB

![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/books_scraper/ci.yml?label=Build) 
![License](https://img.shields.io/github/license/yourusername/books_scraper) 
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue) 
![Scrapy](https://img.shields.io/badge/scrapy-framework-orange) 
![MongoDB](https://img.shields.io/badge/mongodb-database-brightgreen)

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

The scraper is designed to extract book information from [atticbooks.co.ke](https://atticbooks.co.ke/) in the **non-fiction books category**. It:
- Extracts relevant data like book titles and prices.
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
scrapy crawl book
```

The scraper will:
- Start at the specified URL.
- Navigate through the non-fiction books category.
- Extract data and store it in the MongoDB database.

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
- `spiders/book_spider.py`: The main spider responsible for scraping the website.

---

## ✨ Customization

To adapt the scraper for different categories or websites:

1. **Update the `start_urls`**:

   Modify the `start_urls` list in `book_spider.py` to point to the desired category or website.

2. **Adjust the Parsing Logic**:

   Ensure the CSS selectors in the `parse` method of `book_spider.py` accurately target the desired data fields on the new website.

3. **Handle Pagination**:

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
