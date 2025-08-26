def coin_change(coins, amount):
    # 이전에는 dp 배열의 값을 0으로 초기화
    # 이번에는 최적값을 구함: 0으로 초기화하면 안 됨 => 충분히 큰 값
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # i: 현재 거스름돈
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # dp[i-coin]: 내가 선택한 거스름돈에서 해당 coin만큼 뺐을 때 최소 동전의 개수
                # +1은 coin값의 동전 한 개를 더하는 것
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount]

coins = [1, 4, 6]  # 사용 가능한 동전의 종류
amount = 8  # 만들어야 할 금액

print(coin_change(coins, amount))
