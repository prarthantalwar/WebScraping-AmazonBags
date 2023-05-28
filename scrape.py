import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Part 1: Scraping product listing pages
base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"

product_urls = []
product_names = []
product_prices = []
ratings = []
review_counts = []

for page in range(1, 21):  # Scrape 20 pages
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product details
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for product in products:
        # Product URL
        product_url = "https://www.amazon.in" + product.find('a', {'class': 'a-link-normal'})['href']
        product_urls.append(product_url)

        # Product Name
        product_name_element = product.find('span', {'class': 'a-size-base-plus'})
        product_name = product_name_element.text if product_name_element else 'N/A'
        product_names.append(product_name)

        # Product Price
        product_price_element = product.find('span', {'class': 'a-offscreen'})
        product_price = product_price_element.text if product_price_element else 'N/A'
        product_prices.append(product_price)

        # Rating
        rating_element = product.find('span', {'class': 'a-icon-alt'})
        rating = rating_element.text if rating_element else 'N/A'
        ratings.append(rating)

        # Number of Reviews
        review_count_element = product.find('span', {'class': 'a-size-base'})
        review_count = review_count_element.text if review_count_element else 'N/A'
        review_counts.append(review_count)

# Part 2: Scraping individual product pages
descriptions = []
asins = []
product_descriptions = []
manufacturers = []

for product_url in product_urls[:200]:  # Hit 200 product URLs
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Description
    description_element = soup.find('div', {'id': 'productDescription'})
    description = description_element.text.strip() if description_element else 'N/A'
    descriptions.append(description)

    # ASIN
    asin_element = soup.find('th', string='ASIN')
    asin = asin_element.find_next_sibling('td').text.strip() if asin_element else 'N/A'
    asins.append(asin)

    # Product Description
    product_description_element = soup.find('div', {'id': 'feature-bullets'})
    product_description = product_description_element.text.strip() if product_description_element else 'N/A'
    product_descriptions.append(product_description)

    # Manufacturer
    manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
    manufacturer = manufacturer_element.text.strip() if manufacturer_element else 'N/A'
    manufacturers.append(manufacturer)

# Creating a DataFrame from the scraped data
data = {
    'Product URL': product_urls[:200],
    'Product Name': product_names[:200],
    'Product Price': product_prices[:200],
    'Rating': ratings[:200],
    'Number of Reviews': review_counts[:200],
    'Description': descriptions,
    'ASIN': asins,
    'Product Description': product_descriptions,
    'Manufacturer': manufacturers
}

df = pd.DataFrame(data)

# Exporting DataFrame to CSV
df.to_excel('scraped_data.csv', index=False)

