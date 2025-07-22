import re

text = 'My phone number is 123-456-7890.'

# 그룹화
pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(pattern, text)
if match:
    print(match.group(0))  # 매칭된 전체 문자열
    print(match.group(1))  # 첫 번째 그룹에 매칭된 문자열
    print(match.group(2))  # 두 번째 그룹에 매칭된 문자열
    print(match.group(3))  # 세 번째 그룹에 매칭된 문자열
    print(match.groups())  # 모든 그룹에 매칭된 문자열을 튜플로 반환


# 이름 있는 그룹
pattern = r'(?P<area_code>\d{3})-(?P<exchange>\d{3})-(?P<number>\d{4})'
match = re.search(pattern, text)
if match:
    print(match.group('area_code'))
    print(match.group('exchange'))
    print(match.group('number'))
