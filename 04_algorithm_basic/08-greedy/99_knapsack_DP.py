capacity = 30  # 배낭의 최대 무게
items = [(25, 10), (10, 9), (10, 5)] # (무게, 가치)
# items = [(25, 15), (10, 9), (10, 5)] # (무게, 가치)
result = knapsack_dp(capacity, items)
print(f"최대 가치: {result}")