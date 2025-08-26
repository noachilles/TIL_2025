def fibo(N):
    if N  <= 1:
        return N

    # 함수 내에서 저장할 공간 생성
    dp = [0] * (N+1)
    dp[1] = 1

    # N번의 연산으로 값을 구할 수 있음
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]