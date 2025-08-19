"""
완성본: 경로 압축 + 랭크 기반 Union
두 최적화 기법을 모두 적용하여 거의 상수 시간 O(α(N))에 가까운 효율을 달성
실제 알고리즘 문제에서 사용하는 최종 버전
"""

def make_set(n):
    """부모와 랭크 리스트 초기화"""
    pass

def find_set(x):
    """경로 압축이 적용된 find_set"""
    pass

def union(x, y):
    """랭크 기반으로 최적화된 union"""
    pass


parent, rank = make_set(6)

edges = [(1, 2), (2, 3), (4, 5), (5, 6), (3, 4)]

for i, (u, v) in enumerate(edges):
    union(u, v)

print(f"최종 parent: {parent}")
print(f"최종 rank: {rank}")
'''
    최종 완성된 서로배타 집합의 구조는 아래처럼 생겼다.
    [0, 1, 1, 1, 1, 1, 4, 4]
    - 0은 사용하지 않음
                        1 
                      / | \ 
                     2  3  4
                          / \
                         5   6
    - 1은 대표자, 2, 3은 1의 자식, 4는 1의 자식이지만 5, 6의 부모
    - 5, 6은 4의 자식
'''