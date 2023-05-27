# Amazon Product Scraper & Data Extraction

This Python-based web scraping project allows you to extract product data from Amazon India. It consists of two parts: scraping product listing pages and extracting detailed information from individual product URLs.

## Description

The project is designed to scrape product information from Amazon India's website, specifically targeting the "bags" category. It retrieves data such as product URLs, names, prices, ratings, and review counts from multiple pages of product listings. Additionally, it visits individual product URLs to fetch more detailed information, including descriptions, ASIN, product descriptions, and manufacturers.

## Features

- Scrapes at least 20 pages of product listings from the "bags" category on Amazon India.
- Collects product details like URLs, names, prices, ratings, and review counts.
- Extracts additional information, including descriptions, ASIN, product descriptions, and manufacturers, from individual product URLs.
- Stores the collected data in an Excel file for easy analysis and further processing.
- Utilizes the Requests library for making HTTP requests and the BeautifulSoup library for HTML parsing.
- Uses the Pandas library to manipulate and organize the scraped data.
- Provides a simple and easy-to-use interface for running the script and exporting the data.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will also need the following packages:

- requests
- BeautifulSoup
- pandas

You can install the required packages by running the following command:
pip install -r requirements.txt

### Running the Script

1. Clone the repository

2. Navigate to the project directory

3. Run the script


The script will start scraping the product data from Amazon India. The extracted data will be stored in an Excel file named "scraped_data.xlsx" in the same directory.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request.

## Contact

For any questions or inquiries, please contact prarthanrohith@gmail.com.


