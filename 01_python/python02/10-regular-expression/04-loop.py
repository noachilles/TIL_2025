import re

text = 'a B 1 c D 2 e F 333'

# 대문자 알파벳 매칭
print(re.findall(r'[A-Z]', text))

# 숫자 매칭
print(re.findall(r'[0-9]', text))

# 소문자, 대문자, 숫자 매칭
print(re.findall(r'[a-zA-Z0-9]', text))

# 소문자 제외 매칭
print(re.findall(r'[^a-z]', text))

# 숫자 1회 이상 매칭
print(re.findall(r'[0-9]+', text))
