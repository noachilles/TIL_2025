import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    grid = [list(map(int, input().split()))[:N] for _ in range(N)]
    max_sum = 0
    across_down_sum = 0
    across_up_sum = 0
    for i in range(N):
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += grid[i][j]
            col_sum += grid[j][i]
            if i == j:
                across_down_sum += grid[i][j]
            elif j == N - 1 - i:
                across_up_sum += grid[i][j]
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
    if max_sum < across_down_sum:
        max_sum = across_down_sum
    if max_sum < across_up_sum:
        max_sum = across_up_sum
    print(f'#{tc} {max_sum}')