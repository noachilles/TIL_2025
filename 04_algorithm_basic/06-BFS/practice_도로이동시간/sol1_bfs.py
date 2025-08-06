import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    # 너비 우선 탐색 -> queue
    # queue에 넣고 싶은 후보군은 (0, 0)
    queue = deque()
    queue.append((0, 0))    # 시작 정점 후보군에 삽입
    distance[0][0] = 0      # 시작 위치까지 이동거리는 0

    # BFS 탐색
    while queue:    # 후보군이 있는 동안
        row, col = queue.popleft()
        # 이 위치에서 4방향에 대한 탐색
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            # 이제 그 다음 탐색지 data[nx][ny]
            # 그러려면 리스트의 범위를 벗어나지 않아야 함
            # 그리고 이전에 방문한 적 없어야 함
            # 그리고 그 위치가 길이어야
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]:
                # 위 조건을 모두 만족하면 후보군에 들 수 있음
                queue.append((nx, ny))
                # 다음 위치까지 도달하는 비용은, 내 위치보다 1 증가한 값
                distance[nx][ny] = distance[row][col] + 1
                # 도착지점에 도착하면, BFS 특성상 가장 빠르게 도착한 길
                # 그때까지의 비용을 할당하고 종료
                if nx == N-1 and ny == M-1:     # 도착지
                    return
    # 모든 후보군 탐색했지만 return 못함
    return -1

# 데이터 입력
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

# 방문 표시를 할 것 -> 우리의 최종 목적이 무엇?
# 해당 위치까지 도달하는 데 걸린 비용이 얼만지 기록
distance = [[-1] * M for _ in range(N)]

get_road_move_time(0, 0)
for dis in distance:
    print(*dis)