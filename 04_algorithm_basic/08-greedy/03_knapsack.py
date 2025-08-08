def fractional_knapsack_greedy(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)     # 무게당 가격으로 내림차순 정렬

    result = 0
    remain_capacity = capacity

    # 이제 가성비 높은 순으로 정렬되었으니, 차례대로 순회
    for weight, value in items:
        if remain_capacity <= 0:    # 남아있는 무게가 없으면 종료
            break

        # 내 현재 물건 전체를 담을 수 있는 경우
        if remain_capacity >= weight:
            remain_capacity -= weight
            result += value
        # 나눠서 담아야 하는 경우
        else:
            fraction = remain_capacity / weight
            result += value * fraction
            remain_capacity = 0
    return result

capacity = 30  # 배낭의 최대 무게
items = [(5, 50), (10, 60), (20, 140)] # (무게, 가치)
result = fractional_knapsack_greedy(capacity, items)
print(f"최대 가치: {result}")