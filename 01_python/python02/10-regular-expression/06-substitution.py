import re

text = 'Please call 123-456-7890 for assistance.'
pattern = r'\d{3}-\d{3}-\d{4}'
replacement = '[phone number]'
new_text = re.sub(pattern, replacement, text)

print(new_text)  # Please call [phone number] for assistance.


import re


def mask_phone_number(match):
    return f'[{match.group()}]'


text = 'Contact us at 123-456-7890 or 987-654-3210.'
pattern = r'\d{3}-\d{3}-\d{4}'
new_text_with_function = re.sub(pattern, mask_phone_number, text)

print(new_text_with_function)
