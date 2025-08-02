# 30 min
import sys
sys.stdin = open('input.txt')
# 0일 때도 종료 조건에 포함된다. **

from collections import deque

def encode(org_code):
    # 기존 숫자 배열을 queue로 선언함
    queue = deque(org_code)
    # 최종 코드를 구했는지 여부
    is_end = False
    # 마지막 코드를 구할 때까지 반복
    while True:
        # 1 cycle
        for i in range(1, 6):
            item = queue.popleft() - i
            # 마지막 코드를 구하기 위한 조건
            if item <= 0:
                queue.append(0)
                is_end = True
                break
            else:
                queue.append(item)
        # 만약 마지막 코드를 구했다면 while문을 빠져나감
        if is_end:
            break
    # 출력을 위해 queue를 list type으로 변환해 return
    return list(queue)

T = 10
for tc in range(1, T+1):
    input_tc = int(input())
    org_code = list(map(int, input().split()))
    encoded = encode(org_code)
    print(f'#{input_tc}', end=' ')
    print(*encoded)