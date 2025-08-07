# heapq의 우선순위 큐 활용 참고 사이트
# https://docs.python.org/ko/3/library/heapq.html#priority-queue-implementation-notes
# PriorityQueue를 import 할 수도 있음
import heapq

# 빈 우선순위 큐 생성
priority_queue = []

# 우선순위 큐에 요소 추가 (우선순위, 작업)
# 문자열을 집어넣어도 우선순위 판별 잘해줌
heapq.heappush(priority_queue, (3, "3 priority task"))  # 우선순위 3인 작업 추가
heapq.heappush(priority_queue, (1, "1 priority task"))  # 우선순위 1인 작업 추가
heapq.heappush(priority_queue, (2, "2 priority task"))  # 우선순위 2인 작업 추가

# 현재 우선순위 큐의 상태 출력
print(priority_queue)  
# [(1, '1 priority task'), (3, '3 priority task'), (2, '2 priority task')]
# 우선순위가 낮은 숫자일수록 더 높은 우선순위를 가짐

# 우선순위 큐에서 요소를 하나씩 꺼내어 출력
while priority_queue:
    task = heapq.heappop(priority_queue)  # 우선순위가 가장 높은 요소를 꺼냄
    print(task)  # 꺼낸 요소 출력
