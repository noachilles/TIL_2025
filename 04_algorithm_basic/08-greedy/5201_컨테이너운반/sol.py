import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 화물 컨테이너 N개 각각의 무게
    ws = list(map(int, input().split()[:N]))
    # 트럭 M개 각각의 적재 가능 용량
    ts = list(map(int, input().split()[:M]))
    ws.sort(reverse=True)
    ts.sort(reverse=True)
    # 이동 가능한 화물의 용량을 저장하기 위한 변수
    acc = 0
    # N개의 화물을 각각 돌면서
    # container: 화물의 포인터
    # truck: 트럭의 포인터
    w = 0
    t = 0
    while w < N and t < M:
        flag = 0

        # 만약 트럭보다 화물의 용량이 크다면
        if ts[t] < ws[w]:
            # 다음 화물을 가리킨다
            w += 1
            flag = 1
        # 만약 트럭에 화물이 담긴다면
        else:
            # 트럭에 담긴 화물을 확인한다
            # print(f'{tc}: {ws[w]}, {ts[t]}')
            # 누적합에 값을 더하고
            acc += ws[w]
            # 다음 화물을 가리킨다
            w += 1
            # 트럭도 찼기 때문에 다음 트럭을 가리킨다
            t += 1
    print(f'#{tc} {acc}')