from pyepc import decode
import re
epc = '303402b58c00e11b0224a417'
sgtin = decode(epc)
gs1_element_string = sgtin.gs1_element_string
print(sgtin.gs1_element_string)

match = re.search(r'\(01\)(\d+)\(21\)', gs1_element_string)

if match:
    result = match.group(1)  # Extract the matched group
    print(result)  # Output: '00044387009003'
else:
    print("Pattern not found.")
