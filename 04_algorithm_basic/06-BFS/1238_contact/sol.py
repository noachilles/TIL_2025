import sys
sys.stdin = open('input.txt')

from collections import deque

def contact_other(start_vertex):
    global max_level, max_vertex
    queue = deque()
    queue.append((start_vertex, 0))
    # queue에 값이 있는 동안
    while queue:
        # 현재 노드와 현재 레벨을 queue에서 popleft()로 받음
        now, level = queue.popleft()
        # 만약 level이 max_level보다 크다면: max_level을 변경하고 max_vertex 초기화
        if level > max_level:
            max_level = level
            max_vertex = now
        # 만약 현재 최대 레벨이라면 max_vertex를 비교
        elif level == max_level and max_vertex < now:
            max_vertex = now
        # 다음 후보군들을 찾음(인접 리스트에서 해당 노드에 저장된 정보를 받아옴)
        for next in adj_list.get(now, []):
            if next in visited:
                continue
            visited.add(next)
            # 다음 후보군과 다음 레벨을 함께 기록
            queue.append((next, level+1))
    return

T = 10
for tc in range(1, T+1):
    # 입력 데이터 길이와 시작 노드 저장
    L, N = map(int, input().split())
    input_data = list(map(int, input().split()))
    # 인접 리스트 만들기
    adj_list = dict()
    # 방문 기록
    visited = set()
    # max_level과 max_vertex 초기화
    max_level = 0
    max_vertex = 0
    # 인접리스트에 input 값 저장
    for i in range(0, L, 2):
        if adj_list.get(input_data[i]) is None:
            adj_list.update({input_data[i] : [input_data[i+1]]})
        else:
            adj_list[input_data[i]].append(input_data[i+1])

    # BFS로 시작점에서부터 연락 시작
    contact_other(N)
    print(f'#{tc} {max_vertex}')