import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 초깃값 설정: 2X3 크기의 타일이 있으므로 dp[3]까지 정의해야 함
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    # 4부터 N까지
    for i in range(4, N+1):
        # 3칸 이전의 값에 대해서는 2 * 3 블럭을 추가 / 2칸 이전의 값에 대해서는 2 * 2, 가로 2개 총 2개 경우의 수 / 1칸 이전에 대해선 세로 블럭 1개
        dp[i] = dp[i-3] * 1 + dp[i-2] * 2 + dp[i-1] * 1

    print(f'#{tc} {dp[N]}')