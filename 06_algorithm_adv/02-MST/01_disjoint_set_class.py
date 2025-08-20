class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)  # 부모 노드 배열 초기화
        self.rank = [0] * (len(v) + 1)  # 랭크 배열 초기화

    def make_set(self, x):
        self.p[x] = x  # 각 노드가 자기 자신을 부모로 가지도록 초기화
        self.rank[x] = 0  # 초기 랭크는 0

    def find_set(self, x):
        if x != self.p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
            self.p[x] = self.find_set(self.p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)  # 노드 x의 대표자(부모) 찾기
        py = self.find_set(y)  # 노드 y의 대표자(부모) 찾기

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py  # x의 부모를 y의 부모로 설정
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
            else:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
                self.rank[px] += 1  # x의 랭크를 1 증가

disjoint_set = DisjointSet([1, 2, 3, 4, 5, 6])

for i in range(1, len(disjoint_set.p)):
    disjoint_set.make_set(i)
print(disjoint_set.p)  # 초기 부모 노드 배열 출력
print(disjoint_set.rank)  # 초기 랭크 배열 출력
print()

# 간선 추가
edges = [(1, 2), (2, 3), (4, 5), (5, 6), (3, 4)]
# 간선을 통해 유니온 연산 수행
for i, (u, v) in enumerate(edges):
    disjoint_set.union(u, v)
print(disjoint_set.p)       # 최종 부모 노드 배열 출력
print(disjoint_set.rank)    # 최종 랭크 배열 출력
