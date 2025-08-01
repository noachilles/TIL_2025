from collections import deque

total_candy = 20  # 총 마이쮸 개수
queue = deque()  # 사람들을 저장할 큐
queue.append((1, 1))  # 첫 번째 사람과 받을 마이쮸 개수를 큐에 추가

last_person = None  # 마지막으로 마이쮸를 받은 사람을 저장할 변수

while total_candy > 0:  # 마이쮸가 남아 있는 동안 반복
    person, count = queue.popleft()  # 큐에서 사람과 받을 마이쮸 개수를 꺼냄
    
    if total_candy - count <= 0:  # 남은 마이쮸가 현재 사람이 받을 마이쮸 개수보다 적거나 같은 경우
        last_person = person  # 마지막으로 마이쮸를 받은 사람으로 현재 사람을 설정
        break  

    total_candy -= count  # 현재 사람이 받을 마이쮸 개수를 총 마이쮸 개수에서 뺌
    queue.append((person, count + 1))  # 현재 사람은 다음 차례에 받을 마이쮸 개수를 1 증가시켜 큐에 다시 추가
    queue.append((person + 1, 1))  # 다음 사람을 큐에 추가, 받을 마이쮸 개수는 1로 설정

print(f"마지막 마이쮸는 {last_person}번")  # 마지막으로 마이쮸를 받은 사람을 출력
