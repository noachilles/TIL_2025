
def floyd_warshall(graph):
    n = len(graph)  # 전체 노드의 개수
    # 모든 정점을 경유 정점으로 고려
    for k_node in range(n):
        # 시작노드
        for start in range(n):  # 시작노드
            for end in range(n):    # 도착노드
                # D_ik + D_kj < D_ij 이면: 갱신
                Dik = graph[start][k_node]
                Dkj = graph[k_node][end]
                Dij = graph[start][end]
                if Dik + Dkj < Dij:
                    graph[start][end] = Dik + Dkj
    # 음수 사이클 처리
    for i in range(n):
        if graph[i][i] < 0:
            print('음수 사이클이 존재함')
            break

    return graph

INF = float('inf')  # 무한대

# 예시 그래프의 인접 행렬
# 인접행렬 사용 - 각 노드에서 다른 노드로 가는 비용을 갱신하며 조사할 것
adj_matrix = [
    [0, 4, 2, 5, INF],
    [INF, 0, 1, INF, 4],
    [1, 3, 0, 1, 2],
    [-2, INF, INF, 0, 2],
    [INF, -3, 3, 1, 0]
]

# 음수 사이클 확인
# adj_matrix = [
#     [0, -4, 2, 5, INF],
#     [INF, 0, 1, INF, 4],
#     [1, 3, 0, 1, 2],
#     [-2, INF, INF, 0, 2],
#     [INF, -3, 3, 1, 0]
# ]

result = floyd_warshall(adj_matrix)

# 최단 거리 행렬 출력 
for row in result:
    print(row)
