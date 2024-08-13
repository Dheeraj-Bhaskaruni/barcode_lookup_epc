import os
import pandas as pd
from pyepc import decode
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_image_data(root_folder):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    data = []

    driver = webdriver.Chrome()

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        if os.path.isdir(folder_path):
            for sub_folder_name in os.listdir(folder_path):
                sub_folder_path = os.path.join(folder_path, sub_folder_name)

                if os.path.isdir(sub_folder_path):
                    for file_name in os.listdir(sub_folder_path):
                        # Ignore files starting with a dot
                        if not file_name.startswith('.') and os.path.splitext(file_name)[1].lower() in image_extensions:
                            image_name_without_extension = os.path.splitext(file_name)[0]
                            epc = image_name_without_extension
                            try:
                                sgtin = decode(epc)
                                gs1_element_string = sgtin.gs1_element_string
                                match = re.search(r'\(01\)(\d+)\(21\)', gs1_element_string)

                                if match:
                                    result = match.group(1)  # Extract the matched group
                                else:
                                    result = "Pattern not found"
                            except Exception as e:
                                result = f"Error decoding: {e}"

                            h4_text = "N/A"
                            image_src = "N/A"

                            if result != "Pattern not found" and "Error" not in result:
                                try:

                                    driver.get(f"link_to_barcode_lookup_website_with_barcode")

                                    product_details_div = driver.find_element(By.CLASS_NAME, 'col-50.product-details')

                                    h4_element = product_details_div.find_element(By.TAG_NAME, 'h4')
                                    h4_text = h4_element.text

                                    image_element = driver.find_element(By.CSS_SELECTOR, 'div.col-50 img')
                                    image_src = image_element.get_attribute('src')

                                except Exception as e:
                                    h4_text = f"Error: {e}"
                                    image_src = "N/A"

                            # Append the collected data to the list
                            data.append([folder_name, sub_folder_name, image_name_without_extension, result, h4_text,
                                         image_src])

    driver.quit()

    return data


def save_to_excel(data, output_file):
    df = pd.DataFrame(data, columns=['Folder', 'Sub Folder', 'Image Name', 'Result', 'H3 Text', 'Image Src'])
    df.to_excel(output_file, index=False)


# Example usage
root_folder = 'folder'
output_file = 'image_names_with_results_and_web_info.xlsx'

image_data = get_image_data(root_folder)
save_to_excel(image_data, output_file)

print(f"Image names, results, and web scraping data have been saved to {output_file}")
