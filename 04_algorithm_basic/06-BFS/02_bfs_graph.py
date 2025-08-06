from collections import deque

def BFS(start_vertex):
    # visited = [0] * len(nodes)
    visited = set()
    # deque는 첫번째 인자로 iterable 객체를 받음
    queue = deque([start_vertex])
    visited.add(start_vertex)   # 방문 처리
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 모든 노드들에 대해 인덱스 조사
        for next_index in range(len(nodes)):
            if next_index not in visited and adj_matrix[node][next_index]:
                visited.add(next_index)
                queue.append(next_index)

        '''    
        # 인접 리스트 활용
        # 내 인접 리스트에서 인접 정점 찾아서 순회
        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한 적 없다면
            if neighbor not in visited:
                visited.add(neighbor)   # 방문 예정 표시
                queue.append(neighbor) # 결과 표시
        '''

    return result

# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

# 그래프를 직접 그리는 연습이 필요함

# 인접 리스트 형태
adj_list = {node: [] for node in nodes}       # dict comprehension
# 간선 정보와 정점의 index 정보로 adj_list 채워주기
for edge in edges:
    u, v = map(int, edge.split())     # 시작 정점, 도착 정점
    adj_list[nodes[u]].append(nodes[v])
    adj_list[nodes[v]].append(nodes[u])
print(adj_list)
# print(BFS('A'))

# 인접 행렬 형태
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
for edge in edges:
    u, v = edge.split()
    u_index, v_index = int(u), int(v)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1
print(adj_matrix)
print(BFS(0))

