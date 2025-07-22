import re

text = 'Start and end. Start and stop.'

# 문자열의 시작
print(re.findall(r'^Start', text))

# 문자열의 끝
print(re.findall(r'stop$', text))

# 문자열의 끝
print(re.findall(r'stop\.$', text))
