import sys
sys.stdin = open('input.txt')

from itertools import permutations, combinations


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 요리 1세트에 쓸 식재료 조합
    comb_1 = list(combinations(range(N-1), N//2))

    # 요리 2 세트에 쓸 식재료 조합
    comb_2 = []
    # 요리 2세트에 쓸 식재료 조합은
    # 1세트에서 사용하지 않은 조합
    for i in comb_1:
        comb_2.append(tuple(set(range(N)) - set(i)))

    # 요리 1세트에 대한 시너지
    # 요리 1세트에 쓰일 식재료가 0, 1, 2 번째 라면
    # 각 식재료별 시너지는 다음과 같은 형태로 계산
    # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)],
    s1 = []
    for i in comb_1:
        s1.append(list(permutations(i, 2)))

    # 요리2 세트에 대한 시너지
    s2 = []
    for i in comb_2:
        s2.append(list(permutations(i, 2)))

    # 최댓값 설정
    result = sum(sum(data, []))

    for i in range(len(s1)):
        tmp_a, tmp_b = 0, 0
        for j in range(len(s1[i])):
            # 위에서 설정한 각 세트별 시너지 좌푯값으로
            s1_point = s1[i][j]
            s2_point = s2[i][j]

            # 시너지표에 기재된 각 점수를 임시 변수에 더하고
            tmp_a += data[s1_point[0]][s1_point[1]]
            tmp_b += data[s2_point[0]][s2_point[1]]

        # 두 값의 차의 절댓값이 최종 결과보다 작다면
        if abs(tmp_a - tmp_b) < result:
            # 값 변경
            result = abs(tmp_a - tmp_b)
    print(f'#{tc} {result}')