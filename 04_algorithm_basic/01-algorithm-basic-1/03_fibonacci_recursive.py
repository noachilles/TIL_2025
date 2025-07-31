def fibonacci(n):
    # Basis Rule
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 사용 예시
print(fibonacci(10)) # 55를 출력합니다. (피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
