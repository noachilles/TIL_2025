import sys
sys.stdin = open('input.txt')

# 0-1 knapsack 같은 문제
T = int(input())
for tc in range(1, T+1):
    # 박스 크기 N, 상품 개수 M
    N, M = map(int, input().split())
    product_list = [tuple(map(int, input().split())) for _ in range(M)]

    # 박스 크기를 1부터 N까지 만듦
    capacity = [0 for _ in range(N+1)]
    # 각 아이템을 불러옴
    for i in range(M):
        # 아이템의 사이즈, price
        size, price = product_list[i]
        # 최대 용량이 w와 같을 때: 크기는 1씩 줄어듦
        for w in range(N, size-1, -1):
            # 포함 / 미포함(기존 값) 중 더 큰 값을 저장
            capacity[w] = max(price + capacity[w - size], capacity[w])

    print(f'#{tc} {capacity[N]}')