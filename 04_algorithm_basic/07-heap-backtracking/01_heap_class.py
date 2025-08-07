class MinHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화
        self.length = 0  # 힙의 길이 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self.length += 1  # 힙의 길이 증가
        self._siftup(self.length - 1)  # 가장 마지막에 삽입된 요소의 index를 넘김

    # 힙에서 최소 요소를 제거하고 반환
    def heappop(self):  # 리스트의 pop이 되지 않도록 swap 처리
        if self.length == 0:
            raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
        # 루트 노드의 원소를 반환
        root = self.heap[0]
        # 마지막 요소를 루트로 이동
        self.heap[0] = self.heap.pop()
        # 내 길이를 1 감소
        self.length -= 1
        # 힙의 속성을 유지할 수 있도록 siftdown 진행
        self._siftdown(0)
        return root
        
    # 주어진 리스트을 힙으로 변환
    def heapify(self, array):
        self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
        self.length = len(array)
        for i in range(self.length // 2 - 1, -1, -1):
            self._siftdown(i)

    # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftup(self, idx): # '_': 내부적으로 사용할 메소드라는 걸 명시
        # 마지막에 삽입된 노드와 부모 노드의 크기를 비교
        # -> 부모 노드의 인덱스를 얻어야 함
        parent = (idx - 1) // 2     # 인덱스가 0부터 시작하므로
        '''
            최소힙을 구현하는 중
            언제까지 siftup이 이루어져야? 
            1. 내 idx가 0이 되기 전까지
            2. 내 값이 부모 노드의 값보다 작은 동안     
        '''
        # 자식이 부모보다 작은 경우, 교환
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent    # 내 위치를 부모와 swap 했으니 갱신
            parent = (idx - 1) // 2     # 부모 정보 갱신

    # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftdown(self, idx):
        '''
            1. 가장 작은 요소를 무엇으로 볼 것인지 담을 수 있는 변수 초기화
                - 첫 시작 과정에서는 일단 루트를 smallest로 지정
            2. 왼쪽 자식의 인덱스를 계산
            3. 오른쪽 자식의 인덱스를 계산
        '''
        smallest = idx
        left = 2 * idx + 1  # 인덱스 0부터 시작하므로
        right = 2 * idx + 2

        # 왼쪽 자식의 index가 내 전체 크기를 벗어나지 않고
        if left < self.length and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.length and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            # swap한 자리의 자식보다 내가 충분히 클 수 있으니
            # 지금 작업을 계속 반복
            self._siftdown(smallest)

    def __str__(self):
        return str(self.heap)  # 힙의 문자열 표현 반환

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]

min_heap.heapify([5, 4, 3, 2, 1])
print(min_heap)  # [1, 2, 3, 5, 4]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 4, 3, 5] 
print(min_heap.heappop())  # 2
print(min_heap)  # [3, 4, 5]