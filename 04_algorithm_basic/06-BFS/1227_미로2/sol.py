import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_road(start_point):
    # queue를 선언함
    ir, ic = start_point
    queue = deque()
    queue.append((ir, ic))
    # 방문 처리
    visited[ir][ic] = 1
    # queue에 값이 있는 동안
    while queue:
        # 먼저 입력된 칸들을 방문해서
        row, col = queue.popleft()
        # 상하좌우 살피기
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            # 다음 칸이 grid 범위 바깥이면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 벽이면 패스
            elif grid[nr][nc] == 1:
                continue
            # 이미 방문한 기록이 있으면 패스
            elif visited[nr][nc] == 1:
                continue
            # 도착점이면 1을 반환
            if (nr, nc) == end_point:
                return 1
            queue.append((nr, nc))
            visited[nr][nc] = 1
    # 여기까지 왔으면 -1 반환
    return -1

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    grid = [list(map(int, input())) for i in range(N)]
    # 출발점은 2인 지점
    # 도착점은 3인 지점
    # 출발점과 도착점을 각각 찾음
    start_point = (0, 0)
    end_point = (0, 0)
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 출발점일 경우
            if grid[r][c] == 2:
                start_point = (r, c)
            # 도착점일 경우
            elif grid[r][c] == 3:
                end_point = (r, c)
    print(f'#{tc}', end=' ')
    # 출발점에서 시작해 도착점에 도달할 수 있다면 1을 출력
    if find_road(start_point) == 1:
        print(1)
    # 도달하지 못할 경우 0을 출력
    else:
        print(0)