def depth_first_search(node):
    '''
        node: 현재 방문 노드
    '''
    # 현재 노드 방문
    print(node)
    if node not in adj_list:
        return
    # node가 가진 모든 자식 노드드렝 대해 순회
    # 동일한 깊이 우선 탐색
    # for next in adj_list.get(node): # None type은 접근할 수 없음
    for next in adj_list[node]: # 대괄호 접근법을 사용하면 keyerror 발생
        depth_first_search(next)

adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I']
}

depth_first_search('A')