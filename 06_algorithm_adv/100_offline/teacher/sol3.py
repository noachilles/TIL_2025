'''
DP로 풀어봐야겠다 생각했는데, 어떻게 접근하실지 궁금하다
** 쓸데없는 가지치기를 하지 않도록 주의하자
'''

import sys
sys.stdin = open('input.txt')

'''
1~12월까지 각 일자별 사용계획 일
최소비용
'''
T = int(input())
N = 12
for tc in range(1, T+1):
    price = [10, 40, 100, 300]  # 1d, 1m, 3m, 1y
    plan = list(map(int, input().split()))
    # 최적값을 찾기 위해서 3001로 초기화
    acc_price = [[3001 for _ in range(N)] for _ in range(4 + 1)]   # 각 ticket을 적용했을 때 결과를 저장하기 위한 DP
    '''
        1. 제일 바보같은 방법을 생각한다 - 항상 여기서부터 출발하자 - 가장 단순하고 기본적인 방법
        : 전부 1일권으롱 구매했을 때 가격 -> 12월까지 누적되는 가격
    '''
    ticket = 1
    for i in range(N):
        # 이전 ticket까지 포함했을 때
        acc_price[ticket][i] = acc_price[ticket-1][i] + price[ticket-1] * plan[i]
    print(acc_price[ticket])
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