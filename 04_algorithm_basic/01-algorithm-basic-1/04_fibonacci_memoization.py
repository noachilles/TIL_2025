def fibonacci_memoization(n):
    print(memo, n)
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    return memo[n]

n = 10
memo = [0] * (n + 1) # 0부터 10까지니까 총 11개
# 피보나치의 기본룰
memo[0], memo[1] = 0, 1 # 기본 룰 초기화

print(fibonacci_memoization(10))