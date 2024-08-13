import requests
from bs4 import BeautifulSoup

def fetch_product_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)  # Print the status code
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_name_tag = soup.find('h4', class_='product-name')
        if product_name_tag:
            product_name = product_name_tag.text.strip()
            image_tag = soup.find('img', alt=product_name)
            image_url = image_tag['src'] if image_tag else 'No image found'
            return {
                'Product Name': product_name,
                'Image URL': image_url
            }
        else:
            return 'Product details not found'
    else:
        return 'Failed to retrieve page'

# Example usage
barcode = '00044387009003'
details = fetch_product_details(f'link_to_barcode_lookup_website_with_barcode')
print(details)
