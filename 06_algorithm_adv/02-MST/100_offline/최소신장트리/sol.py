import sys
sys.stdin = open('input.txt')

import heapq

def prim():
    mst = []
    global res
    start_vertex = 0
    visited = set()
    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)
    # print(min_heap)
    # 연결된 가장 작은 값들부터 방문
    while min_heap:
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue
        visited.add(end)
        mst.append((start, end, weight))
        res += weight
        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))

    return mst

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]

    # 인접 리스트를 만듦
    adj_list = {v: [] for v in range(V+1)}
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))

    # 답
    res = 0

    # prim을 진행해서 결과를 반환받음
    mst = prim()

    print(f'#{tc} {res}')