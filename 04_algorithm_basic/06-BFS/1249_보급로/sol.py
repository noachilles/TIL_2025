import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_fix_road(r, c):
    global min_acc_time
    queue = deque()
    queue.append((r, c, 0))
    acc_map[r][c] = 0
    while queue:
        # 행, 열, 누적복구시간
        row, col, acc = queue.popleft()
        if row == N-1 and col == N-1:
            if acc < min_acc_time:
                min_acc_time = acc
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if acc_map[nr][nc] == -1:
                    acc_map[nr][nc] = acc + grid[nr][nc]
                    queue.append((nr, nc, acc + grid[nr][nc]))
                # 합이 더 크면
                elif acc_map[nr][nc] > (acc + grid[nr][nc]):
                    acc_map[nr][nr] = acc + grid[nr][nc]
                    queue.append((nr, nc, acc + grid[nr][nc]))
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    min_acc_time = 90000
    acc_map = [[-1] * N for _ in range(N)]
    # 모든 경로를 살피며 최소 복구 시간의 경로를 발견함
    find_fix_road(0, 0)
    print(min_acc_time)