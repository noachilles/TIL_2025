import math
import heapq

# 인접 행렬을 활용한 다익스트라 알고리즘 (우선순위 큐 사용)
def dijkstra_matrix(graph, start):
    n = len(graph)
    distances = [math.inf] * n
    distances[start] = 0
    
    # 우선순위 큐 초기화 (거리, 노드)
    pq = [(0, start)]
    
    # 우선순위 큐에 아무것도 들어있지 않을 때까지 최단거리 갱신 반복 
    while pq:
        # 현재 정점과 해당 정점까지 도달하는 데 걸리는 거리
        curr_dist, curr_node = heapq.heappop(pq)
        
        # 정점까지의 기존 거리보다 갱신된 거리가 크다면 그냥 넘어감
        if distances[curr_node] < curr_dist: continue


        # 인접한 모든 노드 확인
        for next_node in range(n):
            # 인접 리스트와 달리 모든 노드에 대해서 조사 하게 되므로
            # 연결된 노드인지 확인하는 조건이 추가되어야 한다.
            if graph[curr_node][next_node] != math.inf:
                # 새로운 거리 계산
                distance = distances[curr_node] + graph[curr_node][next_node]
                if distance < distances[next_node]: # 새로운 거리가 더 짧으면 갱신
                    distances[next_node] = distance
                    heapq.heappush(pq, (distance, next_node))   # 우선순위 큐에 추가
    
    return distances

# 기존 그래프와 동일한 결과
graph_matrix = [
    [0, 3, 5, math.inf, math.inf, math.inf],
    [math.inf, 0, 2, math.inf, math.inf, math.inf],
    [math.inf, 1, 0, 4, 6, math.inf],
    [math.inf, math.inf, math.inf, 0, 2, 3],
    [math.inf, math.inf, math.inf, math.inf, 0, 6],
    [math.inf, math.inf, math.inf, math.inf, math.inf, 0]
]

start_v = 0
res = dijkstra_matrix(graph_matrix, start_v)
print(res)  # [0, 3, 5, 9, 11, 12] - 동일한 결과