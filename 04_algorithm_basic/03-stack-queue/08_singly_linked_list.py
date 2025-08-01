class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드를 가리키는 포인터

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 헤드 초기화

    # 특정 위치에 노드를 삽입하는 메서드
    def insert(self, data, position):
        pass

    # 리스트의 끝에 노드를 추가하는 메서드
    def append(self, data):
        # 삽입하려고 하는 데이터 토대로 Node 생성
        new_node = Node(data)
        # full은 물어보지 X / empty는 물어보자
        # 만약 비어있는 list라면
        if self.is_empty():
            # 단순히 head가 새로운 node를 가리키도록
            self.head = new_node
        else:
            # 만약 비어있지 않다면 아래처럼 - next 속성이 새로운 노드를 가리키도록
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    # 리스트가 비어있는지 확인하는 메서드
    def is_empty(self):
        pass

    # 특정 위치의 노드를 삭제하는 메서드
    def delete(self, position):
        pass

    # 특정 데이터를 가진 노드의 위치를 찾는 메서드
    def search(self, data):
        pass

    # 리스트를 문자열로 변환하는 메서드
    def __str__(self):
        result = []
        current = self.head
        while current:  # 리스트를 순회하며 데이터를 결과 리스트에 추가
            result.append(current.data)
            current = current.next
        return str(result)  # 결과 리스트를 문자열로 변환하여 반환

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print(sll)  # [1, 2, 3]

# deleted_item = sll.delete(1)# 시간초과 발생
# def goby_bus(road, now, count, battery):
#     global res
#
#     # 만약 배터리가 없다면 돌아감
#     if battery < 0 or res <= M:
#         return
#
#     # 배터리가 모두 닳지 않았으며 현재 위치가 종점이라면
#     if now == N:
#         if res > count:
#             res = count
#         return
#
#     # 만약 현재 위치에 충전소가 없다면
#     if road[now] == 0:
#         # 앞으로 전진만 할 수 있음
#         goby_bus(road, now+1, count, battery-1)
#     # 만약 현재 위치에 충전소가 있다면
#     else:
#         # 앞으로 전진
#         goby_bus(road, now+1, count, battery-1)
#         # 충전 후 전진
#         goby_bus(road, now+1, count+1, K-1)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     road = [0] * (N+1)
#     chargers = list(map(int, input().split()))
#     # chargers의 경로를 road에 저장함
#     for idx in chargers:
#         road[idx] = 1
#     res = M + 1
#     goby_bus(road, 0, 0, K)
#
#     print(f'#{tc}', end=' ')
#     if res > M:
#         print(0)
#     else:
#         print(res)
# print(f"Deleted item: {deleted_item}")  # 2
# print(sll)  # [1, 2, 3]