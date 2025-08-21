import sys
sys.stdin = open('input.txt')

def flowyd_warshall(graph):
    global max_dist
    for k in range(N):
        for start in range(N):
            for end in range(N):
                Dik = graph[start][k]
                Dkj = graph[k][end]
                Dij = graph[start][end]
                if Dij > Dik + Dkj:
                    graph[start][end] = Dik + Dkj
    return graph

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if r != c and graph[r][c] == 0:
                graph[r][c] = float('inf')

    # 답안
    max_dist = -float('inf')

    # i에서 j로 이동할 때 비용이 음수인 사이클은 존재하지 않음
    # 인접 행렬을 활용하는 - 플로이드 워셜을 사용한다
    graph = flowyd_warshall(graph)
    for r in range(N):
        for c in range(N):
            if max_dist < graph[r][c]:
                max_dist = graph[r][c]
    print(f'#{tc} {max_dist}')