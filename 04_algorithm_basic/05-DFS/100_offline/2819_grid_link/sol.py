import sys
sys.stdin = open('input.txt')

# (r,c) : 동 서 남 북
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def depth_first_search(ir, ic, number):
    '''
        ir, ic: 입력 행열정보
        number: 기존 숫자 배열
    '''
    if len(number) == M:
        if number not in numbers_list:
            numbers_list.add(number)
        return

    # 동서남북 각 방향에 대해
    for d in range(4):
        # 다음 칸 정보를 불러오고
        nr, nc = ir + directions[d][0], ic + directions[d][1]
        # 격자판 내의 값일 경우에는 문자열 정보에 해당 값을 추가 및 재귀
        if 0 <= nr < N and 0 <= nc < N:
            new_number = number + str(grid[nr][nc])
            depth_first_search(nr, nc, new_number)

T = int(input())
for tc in range(1, T+1):
    N = 4
    M = 7
    numbers_list = set()
    grid = [list(map(int, input().split()))[:4] for _ in range(4)]
    # 임의의 시작 위치를 정하기 위한 반복문
    for r in range(N):
        for c in range(N):
            chk = []
            depth_first_search(r, c, str(grid[r][c]))

    print(f'#{tc} {len(numbers_list)}')
