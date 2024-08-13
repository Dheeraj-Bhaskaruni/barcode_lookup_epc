from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')


driver = webdriver.Chrome(path="path_to_chrome_driver", options=options)

driver.get("link_to_barcode_lookup_website")
element = driver.find_element(By.NAME, "query")
assert element.is_enabled()
driver.quit()
