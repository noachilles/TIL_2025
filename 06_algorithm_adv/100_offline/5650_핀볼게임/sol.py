import sys
sys.stdin = open('input.txt')

# 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 블럭 경사면 처리
incline = {1: {2: 1, 3: 0},
           2: {3: 2, 0: 1},
           3: {1: 2, 0: 3},
           4: {2: 3, 1: 0},
           5: {}
           }

def simulation(ir, ic, d):
    # 벽에 부딪히는 횟수 & 블록에 부딪히는 횟수
    score = 0
    r, c = ir, ic
    while True:
        # 다음 값을 정함
        nr = r + dr[d]
        nc = c + dc[d]

        # 종료 조건 1: 만약 board 상 다음 지점이 출발 지점이면 종료
        if nr == ir and nc == ic:
            return score

        # 만약 범위를 벗어나면 - 방향 전환: 반대 방향
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            r, c = nr, nc
            d = (d + 2) % 4
            score += 1
            continue

        # 범위 내이면 다음 값을 저장
        nxt = board[nr][nc]

        # 종료 조건 2: 만약 board 상 다음 지점의 값이 -1이면 종료
        if nxt == -1:
            return score
        # 아무것도 없으면 그냥 지나감
        elif nxt == 0:
            r, c = nr, nc
        # 경사면 블록 처리 - incline
        elif nxt <= 5:
            # 수직, 수평면과 부딪히면
            if incline[nxt].get(d) == None:
                d = (d + 2) % 4
            else:
                if nr == r and nc == c:
                    return score
                d = incline[nxt][d]
            r, c = nr, nc
            # 부딪히기만 하면 score +1
            score += 1
        # 웜홀 처리 - worm_whole: (0, 1) (2, 3)
        else:
            if (nr, nc) == worm_whole[nxt][0]:
                r, c = worm_whole[nxt][1]
            else:
                r, c = worm_whole[nxt][0]

T = int(input())
for tc in range(1, T+1):
    # N을 먼저 입력받음
    N = int(input())
    # board 입력
    board = [list(map(int, input().split()))[:N] for _ in range(N)]

    # 웜홀을 각각 쌍 맞춰서 저장 - dict()
    worm_whole = {i:[] for i in range(6, 10+1)}
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 6:
                worm_whole[board[r][c]].append((r, c))

    res = 0
    # 각 위치를 모두 돌면서 모든 방향에서 탐색 시작
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0: continue
            for d in range(4):
                # simulation
                temp = simulation(r, c, d)
                if res < temp:
                    res = temp
    print(f'#{tc} {res}')
