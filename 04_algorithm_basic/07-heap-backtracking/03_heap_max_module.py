# heapq를 최대힙으로 사용하기

import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

max_heap = []
for number in numbers:
    heapq.heappush(max_heap, -number)
print(max_heap)
largest = -heapq.heappop(max_heap)
print(largest)