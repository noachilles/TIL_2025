# python에서는 bin()을 이용해서 이진수로 만들 수 있음
# '0b'가 붙으므로 '0b'이후부터의 값을 조작해 결과 출력

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    binary_code = []
    x = M
    while x > 0:
        binary_code.append(x % 2)
        x //= 2

    flag = False
    cnt = 0
    for i in range(N):
        if i + 1 > len(binary_code):
            break
        if binary_code[i]:
            cnt += 1
    if cnt == N:
        flag = True

    print(f'#{tc}', end=' ')
    if flag:
        print('ON')
    else:
        print('OFF')