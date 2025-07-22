try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# 0으로 나눌 수 없습니다.


try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
"""
숫자입력 : a
숫자가 아닙니다.
"""

# raise: 원하는 값이 나오지 않았을 때 Error를 발생시킬 수 있음  

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
