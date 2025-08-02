class CircularQueue:
    # 원형 큐를 초기화하는 메서드
    def __init__(self, size=5):
        self.size = size  # 큐의 크기
        self.items = [None] * size  # 큐를 지정된 크기의 None 리스트로 초기화
        self.front = -1  # 큐의 앞쪽 인덱스 초기화
        self.rear = -1  # 큐의 뒤쪽 인덱스 초기화

    # 큐에 아이템을 추가하는 메서드
    def enqueue(self, item):
        if self.is_full():  # 큐가 가득 찬 경우
            print("큐가 가득 찼습니다.")  # 경고 메시지 출력
        else:
            if self.front == -1:  # 큐가 비어 있는 경우
                self.front = 0  # front를 0으로 설정
            self.rear = (self.rear + 1) % self.size  # rear 인덱스를 순환하여 증가
            self.items[self.rear] = item  # rear 위치에 아이템 추가

    # 큐에서 아이템을 제거하고 반환하는 메서드
    def dequeue(self):
        if self.front == -1:  # 큐가 비어 있는 경우
            print("큐가 비었습니다.")  # 경고 메시지 출력
            return None
        else:
            dequeued_item = self.items[self.front]  # front 위치의 아이템 제거
            self.items[self.front] = None
            if self.front == self.rear:  # 큐에 하나의 아이템만 있는 경우
                self.front = -1  # 큐를 비움
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size  # front 인덱스를 순환하여 증가
            return dequeued_item

    # 큐의 맨 앞 아이템을 반환하는 메서드
    def peek(self):
        if self.front == -1:  # 큐가 비어 있는 경우
            print("큐가 비었습니다.")  # 경고 메시지 출력
            return None
        else:
            return self.items[self.front]  # front 위치의 아이템 반환

    # 큐가 비어 있는지 확인하는 메서드
    def is_empty(self):
        return self.front == -1  # 큐가 비어 있는지 확인

    # 큐가 가득 찼는지 확인하는 메서드
    def is_full(self):
        return (self.rear + 1) % self.size == self.front  # rear 인덱스가 front 인덱스의 바로 앞에 있는지 확인

# CircularQueue 클래스 테스트
queue = CircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.items)
print(queue.peek())

queue.enqueue(4)
queue.enqueue(5)

print(queue.items)
print(queue.is_full())
queue.enqueue(11)
print(queue.items)
