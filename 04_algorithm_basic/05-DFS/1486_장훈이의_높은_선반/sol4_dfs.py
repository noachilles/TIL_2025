import sys
sys.stdin = open("input.txt")

def dfs(idx, total):
    global min_height
    # 현재 탐색 중인 점원의 index
    # 지금까지 선택한 점원들의 키

    if total >= min_height:
        return

    # idx가 얼마가 되면 종료? N이 될 때까지
    if idx == N:
        # 지금까지 선택된 점원들의 키의 총합이
        if total >= B:
            min_height = min(min_height, total)
        return
    # N이 되지 않았다면, 아직 모든 점원에 대해 탐색하지 않은 것
    dfs(idx + 1, total + arr[idx])
    dfs(idx + 1, total)


T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    dfs(0, 0)
    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")

