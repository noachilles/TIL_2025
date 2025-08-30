import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def link_cores(start, visited, cnt, length):
    # print(visited)
    global max_cnt
    global res
    if start == len(cores):
        # 현재 연결할 수 있는 개수를 받아서
        # 비교 후 length도 갱신
        if max_cnt < cnt:
            max_cnt = cnt
            res = length
        elif max_cnt == cnt and length < res:
            res = length
        return
    # core를 하나씩 확인한다
    r, c = cores[start]

    # 경계에 붙어있지 않은 core들만 확인한다.
    if r > 0 and r < N - 1 and c > 0 and c < N - 1:
        for d in range(4):
            # 해당 방향으로 전원까지 경로 확인!!
            nr, nc = r, c
            # 설치를 위한 방문 경로 저장
            temp = []
            # 경로 가능한지 확인
            possible = True
            while True:
                nr += dr[d]
                nc += dc[d]
                # 만약 범위 벗어나면: 설치 가능
                if not (0 <= nr < N and 0 <= nc < N):
                    break
                # 다른 코어 or 전선 만나면 연결 실패
                if (nr, nc) in visited:
                    possible = False
                    break
                temp.append((nr, nc))
            # 경로가 유효하다면
            if possible:
                # print(temp)
                # 설치함 - 방문 처리
                visited.update(temp)
                link_cores(start+1, visited, cnt + 1, length + len(temp))
                for t in temp:
                    visited.discard(t)
    link_cores(start + 1, visited, cnt, length)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    res = 0

    visited = set()
    cores = list()
    # visited에 값을 넣고 시작한다
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                visited.add((r, c))
                cores.append((r, c))
    # 연결 시작
    link_cores(0, visited, 0, 0)
    print(f'#{tc} {res}')