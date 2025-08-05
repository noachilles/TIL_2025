def DFS(now):
    '''
        now: 현재 방문한 정점 정보
    '''
    # 방문 대상 후보군들을 stack에 삽입해서 관리
    stack = []
    # 현재 지점 방문
    visited.add(now)
    stack.append(now)

    # 순회: 언제까지? stack이 빌 때까지
    while stack:
        target = stack.pop()    # 이번 방문 대상
        print(target)           # LIFO 방문

        # 이번 방문 대상의 인접 리스트 순회
        for next in graph[target]:
            # 그 대상 (traget: A, next: B, C)을 방문한 적 없다면
            if next not in visited:
                visited.add(next)
                stack.append(next)

# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C']
}

start_vertex = 'A'
# 정점 정보를 인덱스로 처리하지 않기 때문에,
# 정점이 가진 정보 자체가 방문 여부를 확인하는 집합에 포함되어 있는지 확인
visited = set() # 방문한 정점을 저장할 집합

DFS(start_vertex)