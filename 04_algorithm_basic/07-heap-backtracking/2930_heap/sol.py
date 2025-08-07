import sys
sys.stdin = open('input.txt')

'''
2개의 연산을 수행하는 프로그램을 구성해야 함
연산 1. 자연수 x를 삽입
연산 2. 최대 힙의 루트 노드 키값을 출력하고, 해당 노드를 삭제
'''
class MaxHeap:
    def __init__(self):
        self.heap = [-1]
        self.length = 0

    # 연산 1. 자연수 x를 삽입
    def heappush(self, x):
        # 마지막 노드에 자연수 x를 삽입함
        self.heap.append(x)
        self.length += 1
        # 위 노드들과 값을 비교해서 _siftup
        self._siftup(self.length)

    # 연산 2. 최대 힙의 루트 노드의 키값을 출력하고, 해당 노드 삭제
    def heappop(self):
        # 만약 heap에 값이 없다면
        if self.length < 1:
            return -1
        else:
            # root에 1번째 항목을 대입하고, 제일 마지막 요소와 switch
            # self.length 값을 1 줄이고, siftdown 수행
            root = self.heap[1]
            self.heap[1] = self.heap[self.length]
            self.heap[self.length] = root
            self.heap.pop()
            self.length -= 1
            self._siftdown(1)
            return root

    # 위 노드들과 값을 비교해 _siftup
    def _siftup(self, idx):
        # idx가 0이 아닐 동안
        # 부모노드와의 값을 비교해서, idx의 값이 더 클 경우 swap
        parent = idx // 2
        while idx > 1 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = idx // 2

    # 아래 노드들과 값을 비교해 아래 값보다 작으면 내려감
    def _siftdown(self, idx):
        biggest = idx
        left_child = idx * 2
        right_child = idx * 2 + 1
        if left_child <= self.length and self.heap[idx] < self.heap[left_child]:
            biggest = left_child
        if right_child <= self.length and self.heap[idx] < self.heap[right_child]:
            biggest = right_child
        # 만약 제일 큰 값의 index가 변경되었다면 부모, 자식 간 swap 후 siftdown 재귀 수행
        if biggest != idx:
            self.heap[biggest], self.heap[idx] = self.heap[idx], self.heap[biggest]
            self._siftdown(biggest)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = MaxHeap()
    result = []
    for _ in range(N):
        input_data = input().split()
        # 만약 값이 하나만 들어온다면
        if len(input_data) == 1:
            # heappop을 수행함
            result.append(heap.heappop())
        # 값이 두 개 들어온다면
        else:
            # heappush를 수행함
            o, x = map(int, input_data)
            heap.heappush(x)
            # 출력 결과가 이상하게 나와서 push결과로 확인 -> pop 로직에 에러
            # print('heappush result: ', heap.heap)
    print(f'#{tc}', end=' ')
    print(*result)