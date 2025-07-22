import re

# 정규표현식을 사용한 간단한 패턴 매칭 예제

pattern = r'\d+'  # 숫자가 하나 이상인 패턴
text = 'There are 24 apples and 42 oranges.'

matches = re.findall(pattern, text)
print(matches)  # ['24', '42']


import re

pattern_raw = r'\d+'  # raw string으로 작성
pattern_normal = '\\d+'  # 일반 문자열로 작성

text = 'There are 24 apples and 42 oranges.'

matches_raw = re.findall(pattern_raw, text)
matches_normal = re.findall(pattern_normal, text)

print(matches_raw)  # ['24', '42']
print(matches_normal)  # ['24', '42']
