import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(start, end, l):
    distances = [float('inf')] * (N + 1)
    visited = set()
    visited.add(start)
    heap = [(0, start)] # heap으로 우선순위 큐 구현
    heapq.heapify(heap)

    while heap:
        # 우선순위 큐의 가장 앞의 값을 가져옴 (min_heap)
        dist, current = heapq.heappop(heap)
        # 기존 거리보다, 갱신된 거리가 더 크고, 이미 방문한 적이 있다면: 패스
        if current in visited and distances[current] < dist: continue
        visited.add(current)
        # current에 연결된 값들을 가져옴
        for nxt, weight in graph[current].items():
            # 만약 distances[nxt]가 current의 dist + weight보다 크다면: 갱신
            next_dist = dist + weight
            if next_dist < distances[nxt]:
                distances[nxt] = next_dist
                # heapq에 push한다.
                heapq.heappush(heap, (distances[nxt], nxt))

    return distances[N]

T = int(input())
for tc in range(1, T+1):
    # 마지막 연결지점 번호 N, 도로 개수 E
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 0 ~ N까지 번호, 0~N까지 이동하는 데 걸리는 최소한의 거리
    # 각 edges로부터 graph를 만들어야 함
    graph = {i: {} for i in range(N+1)}
    for s, e, w in edges:
        graph[s].update({e: w})

    # dijkstra 함수를 사용해 최소 distances를 구함
    start = 0
    res = dijkstra(start, N, N+1)
    print(f'#{tc} {res}')
