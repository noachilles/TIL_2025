import sys
sys.stdin = open('input.txt')

dy = [0, 0, -1]
dx = [-1, 1, 0]

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    grid = [list(map(int, input().split()))[:N] for _ in range(N)]

    # 2에서부터 위로 올라오면서 좌우로 갈 수 있으면 좌우로 이동
    # 마지막 줄에서 2가 위치한 열을 찾음
    # 초기값 설정
    y = N - 1
    x = 0

    for c in range(N):
        if grid[N-1][c] == 2:
            x = c

    # 좌우를 먼저 탐색하고, 아니면 위로 올라감
    while y > 0:
        # print((x, y))
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 1:
                grid[y][x] = -1
                x, y = nx, ny
                break
            else:
                nx -= dx[d]
                ny -= dy[d]
    print(f'#{tc} {x}')