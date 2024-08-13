import os
import pandas as pd
from pyepc import decode
import re


def get_image_data(root_folder):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    data = []

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

                            data.append([folder_name, sub_folder_name, image_name_without_extension, result])

    return data


def save_to_excel(data, output_file):
    df = pd.DataFrame(data, columns=['Folder', 'Sub Folder', 'Image Name', 'Result'])
    df.to_excel(output_file, index=False)


# Example usage
root_folder = 'folder'
output_file = 'image_names_with_results.xlsx'

image_data = get_image_data(root_folder)
save_to_excel(image_data, output_file)

print(f"Image names and results have been saved to {output_file}")
