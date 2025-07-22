import re

text = 'Example 123, demo_789.'

# 임의의 한 문자
print(re.findall(r'.', text))

# 숫자
print(re.findall(r'\d', text))

# 숫자가 아닌 문자
print(re.findall(r'\D', text))

# 단어 문자
print(re.findall(r'\w', text))

# 단어 문자가 아닌 문자
print(re.findall(r'\W', text))

# 공백 문자
print(re.findall(r'\s', text))

# 공백 문자가 아닌 문자
print(re.findall(r'\S', text))
