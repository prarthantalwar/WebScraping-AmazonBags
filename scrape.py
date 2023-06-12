import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#  Scraping product listing pages
product_urls = []
product_names = []
product_prices = []
ratings = []
review_counts = []

for page in range(1, 21):  # Scrape 20 pages
    i=page
    url = f"https://www.amazon.in/s?k=bags&page={i}&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract product details
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for product in products:
        # Product URL
        product_url = "https://www.amazon.in" + product.find('a', {'class': 'a-link-normal'})['href']
        product_urls.append(product_url)

        # Product Name
        product_name_element = product.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).find('span',{'class':'a-size-medium a-color-base a-text-normal'})
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
        review_count_element = product.find('span', {'class': 'a-size-base s-underline-text'})
        review_count = review_count_element.text if review_count_element else 'N/A'
        review_counts.append(int(review_count.replace(',','')))


# Creating a DataFrame from the scraped data
data = {
    'Product URL': product_urls,
    'Product Name': product_names,
    'Product Price ': product_prices,
    'Rating': ratings,
    'Number of Reviews': review_counts
    }

df = pd.DataFrame(data)

# Exporting DataFrame to CSV
df.to_excel('scraped_data.xlsx', index=False)
