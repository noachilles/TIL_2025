import sys
sys.stdin = open('input.txt')
'''
# 2개씩 조합
ab_combs = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]

def get_diff(arr):
    global min_diff
    # 서로 다른 조합 목록을 ab_combs 로부터 불러옴 - index로 저장
    for i1, i2, i3, i4 in ab_combs:
        # a1, a2, b1, b2에 각각의 값들을 저장
        a1, a2, b1, b2 = arr[i1], arr[i2], arr[i3], arr[i4]
        # a와 b에 서로 다른 재료들이 잘 들어가는지 확인
        print(f'a1, a2: {a1}, {a2} / b1, b2: {b1}, {b2} ')

        # a_score와 b_score를 각각 구함
        a_score = grid[a1][a2] + grid[a2][a1]
        b_score = grid[b1][b2] + grid[b2][b1]
        # 연산 값을 확인
        print(f'a_score: {a_score} / b_score: {b_score} ')
        temp_diff = abs(a_score - b_score)
        if temp_diff < min_diff:
            min_diff = temp_diff

def combinations(start, arr, n):
    # 4개를 뽑았다면 출력
    if len(arr) == n:
        print(arr)
        # arr 값에 따라서 2개씩 비교해보기
        get_diff(arr)
        return
    for i in range(start, N):
        combinations(i+1, arr + [i], n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split()))[:N] for _ in range(N)]

    min_diff = 40000

    # 4개의 식재료 조합을 서로 중복 없이 출력한다
    combinations(0, [], 4)
    print(min_diff)

# --- 문제를 잘못 이해함 ---
'''

# 식재료를 받아 음식의 맛을 구하는 함수: get_score()
def get_score(arr):
    total_score = 0
    for i in arr:
        for j in arr:
            # 같은 값이면 넘긴다~
            if i == j:
                continue
            # 조리한다
            total_score += grid[i][j]
    return total_score

# 음식 a와 b에 들어가는 식재료 조합을 구하는 함수 combinations
def combinations(start, a_list, n):
    global min_diff
    # 이미 조사한 적이 있다면 pass
    # TypeError: unhashable tyle: 'list'
    if tuple(a_list) in visited:
        return
    # 만약 N//2개의 식재료를 a에 넣었다면
    if len(a_list) == n:
        # print('A:', a_list)
        # b 음식의 식재료를 구한다
        b_list = [x for x in range(N) if x not in a_list]
        visited.add(tuple(a_list))
        visited.add(tuple(b_list))
        # a 음식의 맛을 구한다
        a_score = get_score(a_list)
        # print('B:', b_list)
        b_score = get_score(b_list)
        diff = abs(a_score - b_score)
        if min_diff > diff:
            min_diff = diff

    for i in range(start, N):
        combinations(i+1, a_list + [i], n)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split()))[:N] for _ in range(N)]

    min_diff = float('inf')

    # 이미 처리한 적 있는 집합을 담아두는 공간
    visited = set()

    # N / 2 개의 음식을 고른다
    # 남은 것들의 시너지를 어떻게 연산할지 생각한다
    combinations(0, [], N//2)
    print(f'#{tc} {min_diff}')