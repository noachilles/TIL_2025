import sys
sys.stdin = open('input.txt')

def bino(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        # j는 k를 기준으로 하며 - i와 k 중에 더 작은 값의 +1까지
        for j in range(min(i, k) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]
# bottom-up 방식
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    # recursive를 기반으로 저장함
    res = bino(n, b)

    print(f'#{tc} {res}')