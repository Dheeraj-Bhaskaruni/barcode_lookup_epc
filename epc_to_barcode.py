from epc.utils import decode_epc
from pyepc import SGTIN

tag = decode_epc('303402b58c00e11b0224a417')  # '0x' prefix is optional

tag_str = str(tag)

split_tag = [part for part in tag_str.replace(".", ":").split(":")]
print(tag)
print(split_tag)

company_prefix = split_tag[4]
indicator = len(split_tag[4])
item_ref = split_tag[5]
serial = split_tag[6]
abc = SGTIN(company_prefix, indicator, item_ref, serial)
print(abc.gtin)