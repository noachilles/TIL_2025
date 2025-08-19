"""
경로 압축(Path Compression) 최적화
find_set을 실행하며 만나는 모든 노드가 대표자를 직접 가리키도록 부모 정보를 갱신
트리의 높이를 효과적으로 압축
"""

def make_set(n):
    return [i for i in range(n+1)]

def find_set_pc(x):
    """경로 압축이 적용된 find_set"""
    if x == parent[x]:
        return parent[x]
    # 아니면?
    # 원소 x의 대표자들, 그 대표자의 대표자로 변경
    parent[x] = find_set_pc(parent[x])
    return parent[x]

def union(x, y):
    """두 집합을 합치기"""
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)
    if root_x != root_y:
        parent[root_y] = root_x



parent = make_set(6)

# 긴 트리 생성
union(5, 6)
union(4, 5)
union(3, 4)
union(2, 3)
union(1, 2)
print(f"긴 트리 상태: {parent}")

# 경로 압축 테스트
find_set_pc(6)
print(f"경로 압축 후: {parent}")