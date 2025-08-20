import heapq

def prim(vertices, edges):
    mst = []
    visited = set()
    start_vertex = vertices[0]

    # heapq에 삽입
    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap) # 원소들의 첫 번째 값을 기준으로 하기 때문에 - heapq에 값 넣을 때 주의
    visited.add(start_vertex)

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue

        visited.add(end)    # 새로운 정점 방문
        mst.append((start, end, weight))    # 이 간선 정보 mst에 추가

        for next, weight in adj_list[end]:
            # 현재 도착정점에서 이어진 인접 정점이
            # 다음에 방문할 예정이었던 정점이 이미 방문한 적 있다면
            # 후보군에 넣을 필요도 없다
            if next in visited: continue
            # 지금의 end가 다음의 start가 되므로 - end, next 순서
            heapq.heappush(min_heap, (weight, end, next))
    return mst


'''
    가중치 그래프 형상
         1
      ¹ / \ ²
       2---3
         ³
'''
vertices = [1, 2, 3]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
# 그래프 기준, 인접 정점 정보를 갖고 있어야 함
# => 인접 행렬 or 인접 리스트
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))  # 무방향이어서
print(adj_list)

'''
    MST 구성 결과
         1
      ¹ / \ ²
       2   3
'''
mst = prim(vertices, edges)  # [(1, 2, 1), (1, 3, 2)]
print(mst)


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
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))  # 무방향이어서
print(adj_list)

result = prim(vertices, edges)
print(result) # [(0, 2, 31), (2, 1, 21), (2, 6, 25), (2, 4, 46), (4, 3, 34), (3, 5, 18)]