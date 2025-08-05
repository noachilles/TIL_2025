import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    # 부분 집합의 모든 경우의 수
    subset_cnt = 2 ** N
    for i in range(1, subset_cnt):  # 최소 한 명은 선택해야 하므로 1부터
        h_sum = 0
        for j in range(N):
            # 각 부분 집합
            if i & (1 << j):    # i번째 경우의 수에 j 요소가 선택되었나
                h_sum += arr[j] # 선택되면 점원의 키들을 합함
        if h_sum >= B:
            min_height = min(min_height, h_sum)

    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")