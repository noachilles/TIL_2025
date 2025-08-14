import sys
sys.stdin = open('input.txt')

def coloring(lr, lc, rr, rc, color):
    for r in range(lr, rr+1):
        for c in range(lc, rc+1):
            paper[r][c] += color

T = int(input())
for tc in range(1, T+1):
    # 칠할 영역의 개수 N이 주어짐
    N = int(input())
    # 칠할 영역의 범위 정보를 담은 list
    # 칠할 영역의 범위가 왼쪽 코너부터 오른쪽 코너까지 주어짐
    colored = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 도화지
    paper = [[0] * 10 for _ in range(10)]
    for i in range(N):
        # 좌상단 행, 열, 우하단 행, 열, 색깔정보
        lr, lc, rr, rc, color = colored[i]
        coloring(lr, lc, rr, rc, color)

    for i in range(10):
        for j in range(10):
            if paper[i][j] >= 3:
                cnt += 1
    print(f'#{tc} {cnt}')