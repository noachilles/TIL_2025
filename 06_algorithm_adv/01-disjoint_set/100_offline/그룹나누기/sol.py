# 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람 출석번호 종이에 적어 제출
# 인원 제한 X: 한 사람이 여러 장의 종이를 제출 or 여러 사람이 한 사람 지목한 경우 모두 같은 조

import sys
sys.stdin = open('input.txt')

def make_set(n):
    return [i for i in range(n+1)]

# 자신이 속한 집합의 루트 노드를 반환함
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_x] = root_y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # set의 root 초기화
    parent = make_set(N)

    # union할 목록 저장
    input_data = list(map(int, input().split()))
    union_sets = []
    for i in range(0, 2 * M, 2):
        union_sets.append((input_data[i], input_data[i+1]))

    # 목록의 조합에 대해 union 진행
    for i in range(len(union_sets)):
        x, y = union_sets[i]
        union(x, y)

    # 조의 개수를 구하기 위한 set, cnt를 선언
    cnt = set()
    # 1부터 N까지의 요소를 살피며 cnt에 요소를 add
    for i in range(1, N+1):
        cnt.add(find_set(i))
    print(f'#{tc} {len(cnt)}')
