def knapsack(weights, values, capacity):
    n = len(weights)  # 물건의 개수
    # DP 테이블 초기화: (n+1) x (capacity+1) 크기의 2차원 리스트를 0으로 초기화
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):  # 1부터 n까지
        for w in range(1, capacity + 1):  # 1부터 capacity까지
            if weights[i - 1] > w:  # 현재 물건을 담을 수 없는 경우 = 현재 물건의 무게가 현재 배낭 용량보다 크다면
                K[i][w] = K[i - 1][w]  # 이전 물건까지의 최대 가치를 그대로 가져옴 - 물건이 행 정보 = 앞의 행의 동일한 열의 값을 그대로 가져옴
            else:  # 현재 물건을 담을 수 있는 경우 = 현재 물건의 무게가 현재 배낭 용량보다 작거나 같다면
                # 현재 물건을 담는 경우와 담지 않는 경우 중 최대 가치를 선택
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            # 용량이 w일 때 담을 수 있는 최대 가치 비교: 현재 물건을 담기 전 최댓값 + 현재 물건의 value & 이전 물건까지의 가치 (행 기준)
            # 현재 물건 담기 전 최댓값도 이전 행에서 불러온다: 물건을 중복해서 담을 가능성이 있기 때문에
            print(f'when capacity is {w} and item is {i}: {K[i]}\n 현재 물건 담기 전: {K[i-1][w-weights[i-1]]}, 이전 물건까지의 가치: {K[i-1][w]}')

    return K[n][capacity]  # 최대 담을 수 있는 가치 반환


weights = [50, 10, 30]
values = [120, 100, 120]
capacity = 50  # 배낭의 용량

max_value = knapsack(weights, values, capacity)
print(f"배낭에 담을 수 있는 물건들의 최대 가치: {max_value}")
