import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    dp = [1 for _ in range(N)]
    res = 1

    # O(N^2) 사실 시간 초과를 야기할 것 같지는 않음
    # 각 요소에 대해서
    for i in range(1, N):
        # 앞의 요소가 더 작은 값이면 그 때의 값에 1을 더함 - 그 중에 제일 큰 값을 가져와야 함
        for j in range(i, -1, -1):
            if A[j] < A[i]:
                if dp[j] < res: continue
                # dp[j]를 받아와서 1을 더한 값을 dp[i]에 갱신
                dp[i] = dp[j] + 1
                res = dp[i]

    print(f'#{tc} {res}')