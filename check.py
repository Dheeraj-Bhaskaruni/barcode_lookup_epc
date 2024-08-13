from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("link_to_barcode_lookup_website_with_barcode")


product_details_div = driver.find_element(By.CLASS_NAME, 'col-50.product-details')


h4_element = product_details_div.find_element(By.TAG_NAME, 'h1')


print("H4 Text:", h4_element.text)


image_element = driver.find_element(By.CSS_SELECTOR, 'div.col-30 img')

image_src = image_element.get_attribute('src')



print("Image Src:", image_src)



driver.quit()
