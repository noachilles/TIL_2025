def fibo(N):
    global cnt
    cnt += 1
    # 2보다 크거나 같고 0의 값을 갖고 있다면
    if N >= 2 and memo[N] == 0:
        # memo[N] = memo[N-1] + memo[N-2]
        memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

memo = [0] * (101)  # 100을 구할 것이기 때문에
# f(100)을 얻기 위해서는 f(99), f(98)을 얻을 수 있어야
memo[0] = 0
memo[1] = 1
cnt = 0
result = fibo(100)
print(result)
print(cnt)
