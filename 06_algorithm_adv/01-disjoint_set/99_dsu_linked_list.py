"""
연결 리스트 기반 서로소 집합 구현
각 원소는 Node 객체로 표현되고, 연결 리스트로 집합을 관리
"""

class Node:
    """연결 리스트의 노드"""
    def __init__(self, data):
        self.data = data      # 노드 값
        self.rep = self       # 집합의 대표자, 초기값은 자기 자신
        self.next = None      # 다음 노드 포인터

    def __repr__(self):
        rep_data = self.rep.data if self.rep else None
        next_data = self.next.data if self.next else None
        return f"Node(data='{self.data}', rep='{rep_data}', next='{next_data}')"

def make_set(sets_map, data):
    """새로운 집합 생성"""
    if data not in sets_map:
        sets_map[data] = Node(data)

def find_set(sets_map, data):
    """집합의 대표자 반환"""
    if data in sets_map:
        return sets_map[data].rep
    return None

def union(sets_map, data1, data2):
    """두 집합을 합치기"""
    rep_node1 = find_set(sets_map, data1)
    rep_node2 = find_set(sets_map, data2)

    if rep_node1 is None or rep_node2 is None or rep_node1 == rep_node2:
        return

    # 첫 번째 리스트의 마지막 노드 찾기
    tail_node1 = rep_node1
    while tail_node1.next is not None:
        tail_node1 = tail_node1.next
    
    # 두 리스트 연결
    tail_node1.next = rep_node2

    # 두 번째 리스트의 모든 노드의 대표자를 첫 번째 리스트의 대표자로 갱신
    current_node = rep_node2
    while current_node is not None:
        current_node.rep = rep_node1
        current_node = current_node.next

def print_all_sets(sets_map):
    """모든 노드 상태 출력"""
    print("{")
    for data, node in sets_map.items():
        print(f"  '{data}': {node}")
    print("}")


# 초기화
sets_map = {}
elements = ['a', 'b', 'c', 'd', 'e', 'f']

for elem in elements:
    make_set(sets_map, elem)

print("초기 상태:")
print_all_sets(sets_map)

print("union('a', 'c') 후:")
union(sets_map, 'a', 'c')
print_all_sets(sets_map)

print("union('b', 'd') 후:")
union(sets_map, 'b', 'd')
print_all_sets(sets_map)

print("union('a', 'b') 후:")
union(sets_map, 'a', 'b')
print_all_sets(sets_map)

print("최종 대표자:")
rep_of_a = find_set(sets_map, 'a')
rep_of_d = find_set(sets_map, 'd')
print(f"'a'의 대표자: '{rep_of_a.data}'")
print(f"'d'의 대표자: '{rep_of_d.data}'")