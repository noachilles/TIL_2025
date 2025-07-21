num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언 - 일반적으로 함수 내에서 전역 변수 수정하려고 할 때 사용
    num += 1 # global 키워드 선언 전 참조 불가

print(num)  # 0
increment()
print(num)  # 1
