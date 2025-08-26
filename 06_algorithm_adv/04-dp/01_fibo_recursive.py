def fibonacci(n):
    global cnt
    cnt += 1
    # 기본 규칙: n이 2미만 일때, n을 반환.
    if n < 2:
        return n

    # 귀납 규칙: n이 2 이상일 때, F(n-1) + F(n-2)를 반환
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
cnt = 0
# 사용 예시
print(fibonacci(50)) # 55를 출력
print(cnt)