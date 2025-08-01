class Stack:
    # 생성자 함수
    def __init__(self, capacity=10):
        self.capacity = capacity # 이 자료구조의 최대 수용 가능 공간
        self.items = [None] * capacity
        self.top = -1
        # 왜 top이 0이 아닌 -1로 초기화 하느냐?
        # 여기서 -1은 리스트의 마지막을 의미하는 게 아니라,
        # push 연산을 진행할 때, top의 값을 1 증가시키고, 그곳에 값을 삽입 - 왜일까,,
        # 그냥 처음부터 빈공간을 가리키면 되지 않아? -> pop 구현이 더 편리함 but 0으로도 구현해보자

    # 주어진 값을 삽입
    def push(self, item):
        # 예외 처리: IndexError 방지 / is_full 하다면, 어떠한 처리
        if self.is_full():
            print('Stack is Full')
            # raise IndexError('Stack is Full')

        self.top += 1 # 올바른 삽입 위치 찾기
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def is_full(self):
        return self.capacity -1 == self.top

    def is_empty(self):
        return self.top == -1

# stack 자료구조 인스턴스 생성시, 이 자료구조의 최대 크기도 함께 넘겨줘야 한다.
stack = Stack()
print(stack.items)

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
