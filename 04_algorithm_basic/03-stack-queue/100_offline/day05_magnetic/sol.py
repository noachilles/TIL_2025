# 풀이 20min
import sys
sys.stdin = open('input.txt')

def get_agglutination(grid):
    # S극 자성체를 넣어둘 stack
    stack = []
    # 총 교착 개수를 저장하는 cnt
    cnt = 0
    # 각 열별로 순회
    for c in range(N):
        # 각 행별로 순회
        for r in range(N):
            # 만약 N극 자성체라면 확인을 위해 stack에 추가한다.
            if grid[r][c] == 1:
                stack.append(grid[r][c])
            # 만약 S극 자성체라면
            elif grid[r][c] == 2:
                # stack에 있는 N극 자성체와 교착 상태를 가지므로 N극을 stack에서 제거하고 cnt를 증가
                # 하지만 stack에 N극 자성체가 없다면 바닥으로 떨어진다
                if stack:
                    while stack:
                        stack.pop()
                    cnt += 1
        # 하나의 열을 모두 돌았는데 남아있는 자성체가 있다면
        # 바닥으로 떨어지는 N극이므로 삭제한다
        while stack:
            stack.pop()
    return cnt



T = 10
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', end=' ')
    print(get_agglutination(grid))