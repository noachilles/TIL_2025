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

def mst_kruskal(vertices, edges):
    '''
        1. 가중치를 오름차순 정렬
        2. 그 순서대로 간선 선택
        3. 2에서 선택한 간선의 시작, 종료 노드가 같은 대표자가 아니어야 함
        4. 2와 3을 반복(간선이 n-1개가 될 때까지)
    '''

    mst = []    #  최소 신장 트리
    # 간선의 정보 구성 [[시작노드, 종료노드, 가중치]]
    edges.sort(key=lambda x: x[2])
    print(edges)
    ds = DisjointSet(vertices)  # disjointset 생성
    for i in range(len(vertices) + 1):
        ds.make_set(i)
    print(ds.p)
    for edge in edges:
        print(edge, mst)
        s, e, w = edge  # 시작노드, 끝노드, 가중치
        '''
            가중치에 대한 정보는 처음 오름차순 과정에서 역할 다함
            이제 우리가 할 일은 s와 e가 같은 집합에 속해있는지 판별
            만약 같은 집합에 속하지 않으면 합치기
        '''
        # 두 노드가 다른 집합에 속함 - disjoint로 이를 판단(find_set)
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(edge)
    return mst

'''
    가중치 그래프 형상
         1
      ¹ / \ ²
       2---3
         ³
'''
# [시작정점, 도착정점, 가중치]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertices = [1, 2, 3]  # 정점 집합


'''
    MST 구성 결과
         1
      ¹ / \ ²
       2   3
'''
result = mst_kruskal(vertices, edges)  # [[1, 2, 1], [1, 3, 2]]
print(result)


# 교재 간선 정보
edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))  # 정점 집합

result = mst_kruskal(vertices, edges)
# print(result) # [(3, 5, 18), (1, 2, 21), (2, 6, 25), (0, 2, 31), (3, 4, 34), (2, 4, 46)]