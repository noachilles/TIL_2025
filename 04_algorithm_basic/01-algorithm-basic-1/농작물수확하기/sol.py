import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 농장의 크기 N - 항상 홀수
    # 중심 index는 N // 2
    # 중심 행에서 시작해서 위아래로 갈수록 범위를 2씩 좁힘
    N = int(input())
    mid = N // 2
    grid = [list(map(int, input()))[:N] for _ in range(N)]
    # 누적 수확값
    acc = 0

    # 열 조사 범위를 지정(중앙으로부터 k만큼 +-)
    k = 0
    for r in range(N):
        for c in range(mid - k, mid + k + 1):
            acc += grid[r][c]
        # 만약 N // 2 보다 작다면 늘어남
        if r < N // 2:
            k += 1
        else:
            k -= 1
    print(f'#{tc} {acc}')