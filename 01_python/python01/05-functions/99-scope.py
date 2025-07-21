a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)  # 10 2 500
    local(500)
    print(a, b, c)  # 10 2 3
enclosed()
print(a, b)  # 1 2

# 1. built-in scope: 파이썬 실행 이후부터 영원히 유지
# 2. global scope: 모듈이 호출된 시점 이후 혹은 인터프리터 끝날 때까지 유지
# 3. local scope: 함수 호출될 때 생성되고, 함수 종료될 때까지 유지

# LEGB Rule
# 1. Local scope: 현재 작업 중인 범위
# 2. Enclosed scope: 지역 범위 한 단계 위 범위
# 3. Global scope: 최상단에 위치한 범위
# 4. Built-in scope: 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)
