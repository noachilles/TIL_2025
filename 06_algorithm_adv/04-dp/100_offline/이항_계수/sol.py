import sys
sys.stdin = open('input.txt')

def bino(n, k):
    # 안에 계수를 저장하는 리스트를 만듦
    if k == 0 or k == n:
        return 1
    return bino(n-1, k-1) + bino(n-1, k)

T = int(input())
for tc in range(1, T+1):
    # n, a, b가 주어지면 (x+y)^n에서 x^a*y^b의 계수를 구하는 program
    n, a, b = map(int, input().split())

    # C(n, k) = C(n-1, k) + C(n-1, k-1)
    # 함수를 실행한다
    res = bino(n, b)  # b를 넣어서 구한다
    print(f'#{tc} {res}')