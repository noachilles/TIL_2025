# 43min

from collections import deque

def cut_sticks(chars):
    # 전체 스틱 개수
    total = 0
    # 현재 레이저에 의해 잘리는 막대 개수
    nums = 0
    # 이전값, 현재값
    pre = ''
    now = ''
    queue = deque(chars)
    # queue에 값이 있으면
    while queue:
        # now에 popleft
        now = queue.popleft()
        # 여는 괄호이면 현재 쇠막대 개수 + 1
        if now == '(':
            nums += 1
        # 닫는 괄호이면 현재 쇠막대 개수 - 1 (레이저여도, 쇠막대여도 -1 해야함)
        elif now == ')':
            nums -= 1
            # 만약 여는 괄호와 연속하면 - 레이저이면: 현재 레이저 아래에 있는 쇠막대 개수만큼 절단되어 total에 추가
            if pre == '(':
                total += nums
            # 만약 여는 괄호와 연속하지 않으면 - 막대가 하나 끝난 것이므로: total에 1 추가
            else:
                total += 1
        pre = now
    return total

T = int(input())
for tc in range(1, T+1):
    input_chars = input().strip()
    sticks = cut_sticks(input_chars)
    print(f'#{tc}', end=' ')
    print(sticks)