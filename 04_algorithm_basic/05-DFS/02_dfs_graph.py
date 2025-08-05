def depth_first_search(vertex):
    '''
        vertex: 현재 방문 정점의 index
    '''
    global visited
    # 정점 방문
    # F/T가 저장된 배열을 가리키는 변수가 visited -> 참조하는 값을 변경하는 것이기 때문에
    # local의 새로운 변수가 선언되거나 변경되지 않고 정상작동됨
    visited[vertex] = True
    print(graph[vertex])

    # 현재 정점이 진출할 수 있을 후보군들을 찾음
    # 인접 행렬의 vertex번째 리스트 순회
    for idx in range(N):
    # for candidate in adj_matrix[vertex]:
        # 진출 후보군 A~G 중에, 가능한 경우에 대해서만 (내가 진출 가능한 후보군)
        # 내가 진출 가능한 idx인지 확인하고
        # 그 idx번째가 이전에 방문한 적이 있는지 확인 (방문한 적 없다면)
        if adj_matrix[vertex][idx] and visited[idx] == False:
            depth_first_search(idx)

        # 0    1    2    3    4    5    6
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 정점 수: N
N = 7
# 해당 정점 방문 여부 표시: False로 초기화
visited = [False] * N

# 인접 행렬
adj_matrix = [
#    A  B  C  D  E  F  G
    [0, 1, 1, 0, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0, 0],  # B
    [1, 0, 0, 0, 1, 0, 0],  # C
    [0, 1, 0, 0, 0, 1, 0],  # D
    [0, 1, 1, 0, 0, 1, 0],  # E
    [0, 0, 0, 0, 1, 0, 1],  # F
    [0, 0, 0, 0, 0, 1, 0],  # G
]

# 시작 정점을 0번인 A부터 시작
depth_first_search(0)