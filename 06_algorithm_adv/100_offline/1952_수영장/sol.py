'''
DP로 풀어봐야겠다 생각했는데, 어떻게 접근하실지 궁금하다
** 쓸데없는 가지치기를 하지 않도록 주의하자
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
N = 12
for tc in range(1, T+1):

    day, month, quater, year = map(int, input().split())
    plan = list(map(int, input().split()))

    money = [3001 for _ in range(N)]
    # 0을 초기화
    money[0] = min(month, day * plan[0])
    for i in range(1, N):
        money[i] = money[i-1] + min(month, day * plan[i])

    # 만약 quater 금액권을 결제하면 그 이전달(3달 전)의 최소비용과의 누적합을 구해줘야 함
    # - 한편, month별로 구하면 한 달 전의 누적합에 더해줘야
    money[2] = min(quater, money[2])
    for i in range(3, N):
        money[i] = min(money[i-1] + min(month, day * plan[i]), money[i-3] + quater)

    res = money[N-1]
    # year과 비교
    if res > year:
        res = year

    print(f'#{tc} {res}')
'''
1~12월까지 각 일자별 사용계획 일
최소비용
'''
'''
    1. 제일 바보같은 방법을 생각한다 - 항상 여기서부터 출발하자 - 가장 단순하고 기본적인 방법
    : 전부 1일권으롱 구매했을 때 가격 -> 12월까지 누적되는 가격
'''
'''
    2. 그 다음으로 효율적인 방법
    : 1달 금액으로 샀을 때, 이전 바보같은 방법보다 싸면 바꾸기
'''
'''
    3. 그 다음으로 효율적인 방법
    : 3달 금액으로 샀을 때~
'''
'''
    4. 1년치 사는 거랑 위의 제일 효율적인 방법 누적 금액과 비교

out 12월달까지 누적 최소 금액 
'''
