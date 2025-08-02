from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())
print(queue.popleft())
print(queue)
print(queue[0])

queue.append(4)
queue.append(5)

print(queue)
queue.append(11)