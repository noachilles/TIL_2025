import sys
sys.stdin = open('input.txt')

def get_hamburger(idx, score_sum, kcal_sum):
    global max_score_burger
    # 가지치기 : 현재 값을 추가할 수 있는지 확인
    if kcal_sum > L:
        return
    # 종료조건: 현재 idx가 N-1이라면
    if idx == N:
        if score_sum > max_score_burger:
            max_score_burger = score_sum
        return
    # 모든 조합을 떠올려본다
    new_kcal_sum = kcal_sum + grocery[idx][1]
    get_hamburger(idx + 1, score_sum + grocery[idx][0], new_kcal_sum)
    get_hamburger(idx + 1, score_sum, kcal_sum)

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    grocery = []
    for _ in range(N):
        grocery.append(tuple(map(int, input().split())))

    max_score_burger = -1
    # 햄버거의 점수를 비교한다
    get_hamburger(0, 0, 0)
    print(f'#{tc} {max_score_burger}')