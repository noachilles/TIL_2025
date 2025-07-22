import re

# 이메일 주소 검증
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
emails = ['test@example.com', 'invalid-email', 'user.name@domain.co']
for email in emails:
    if re.search(email_pattern, email):
        print(f'{email} is valid')
    else:
        print(f'{email} is invalid')

# Gmail 주소 검증
gmail_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
emails = [
    'test@gmail.com',
    'user.name@gmail.com',
    'invalid-email',
    'user@domain.com',
]
for email in emails:
    if re.search(gmail_pattern, email):
        print(f'{email} is a valid Gmail address')
    else:
        print(f'{email} is not a valid Gmail address')


# 전화번호 검증
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
phones = ['123-456-7890', '123-45-6789', '123-4567-890']
for phone in phones:
    if re.search(phone_pattern, phone):
        print(f'{phone} is valid')
    else:
        print(f'{phone} is invalid')

# 010으로 시작하는 전화번호 검증
phone_pattern = r'^010-\d{3,4}-\d{4}$'
phones = ['010-1234-5678', '010-234-5678', '011-345-6789', '010-4567-8901']
for phone in phones:
    if re.search(phone_pattern, phone):
        print(f'{phone} is a valid number')
    else:
        print(f'{phone} is not a valid number')

# URL 검증
url_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
urls = ['http://example.com', 'https://www.example.com/path', 'invalid-url']
for url in urls:
    if re.search(url_pattern, url):
        print(f'{url} is valid')
    else:
        print(f'{url} is invalid')
