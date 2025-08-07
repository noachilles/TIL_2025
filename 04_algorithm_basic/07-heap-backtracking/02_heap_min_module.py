import heapq    # 기본적으로 MinHeap이다.

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

# 리스트를 최소 힙으로 변환
heapq.heapify(numbers)
print(numbers)

heapq.heappush(numbers, -1)
print(numbers)

smallest = heapq.heappop(numbers)
print(smallest)
print(numbers)

# heapq로 만들어놓고 append 하면 다소 곤란해짐
numbers.append(-1)
print(numbers)
