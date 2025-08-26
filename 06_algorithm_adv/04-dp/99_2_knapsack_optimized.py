def knapsack_optimized(weights, values, capacity):
    # 1차원 DP 테이블 초기화 - 2차원 리스트로 인한 메모리 낭비 줄이기 위해
    # dp[w]는 현재 용량 w에서의 최대 가치를 저장
    dp = [0] * (capacity + 1)

    # 물건들을 하나씩 순회
    for i in range(len(weights)):
        # 용량 w를 capacity부터 1까지 역순으로 순회 - 모든 범위를 돌지 않고, 해당 item을 담을 수 없을 때까지(if weight가 20이라면 20까지만 반복)
        for w in range(capacity, weights[i] - 1, -1):
            # 현재 물건을 담는 경우와 담지 않는 경우 중 더 큰 가치를 선택
            dp[w] = max(values[i] + dp[w - weights[i]], dp[w])
            print(f'when capacity is {w}: {dp[w]}')

    return dp[capacity]


# 예시
weights = [50, 10, 30]
values = [120, 100, 120]
capacity = 50

max_value = knapsack_optimized(weights, values, capacity)
print(f"최적화된 배낭 문제의 최대 가치: {max_value}")