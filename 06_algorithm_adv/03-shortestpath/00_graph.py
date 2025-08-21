# 정점 정보
vertices = ['a', 'b', 'c', 'd', 'e', 'f']

# 간선 정보
# 시작 정점, 도착 정점, 가중치
edges = [
    (0, 1, 3),
    (0, 2, 5),
    (1, 2, 2),
    (2, 1, 1),
    (2, 3, 4),
    (2, 4, 6),
    (3, 4, 2),
    (3, 5, 3),
    (4, 5, 6)
]

# 인접 리스트
adj_list = {vertices[idx]: {} for idx in range(len(vertices))}
print(adj_list)
for start, end, weight in edges:
    print(start, end, weight)
    print(vertices[start], vertices[end], weight)
    adj_list[vertices[start]][vertices[end]] = weight

'''
{
    'a': {'b': 3, 'c': 5},
    'b': {'c': 2},
    'c': {'b': 1, 'd': 4, 'e': 6},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 6},
    'f': {}
}
'''

# 인접 행렬
adj_matrix = [[float('inf')] * len(vertices) for _ in range(len(vertices))]
# 자기 자신은 도달하지 못하므로 0으로 초기화 해주면 좋겠다
for i in range(len(vertices)):
    adj_matrix[i][i] = 0
for m in adj_matrix:
    print(m)

'''
[
    [0, 3, 5, inf, inf, inf],
    [inf, 0, 2, inf, inf, inf],
    [inf, 1, 0, 4, 6, inf],
    [inf, inf, inf, 0, 2, 3],
    [inf, inf, inf, inf, 0, 6],
    [inf, inf, inf, inf, inf, 0]
]
'''