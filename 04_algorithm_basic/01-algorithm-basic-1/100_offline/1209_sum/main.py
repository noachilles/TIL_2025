import sys
sys.stdin = open('input.txt')

# 이 문제는 10개의 TC를 갖는다.
for _ in range(1, 11):
    tc = input()
    data = [list(map(int, input().split())) for _ in range(100)]

    mx_sum = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        across_sum = 0
        for j in range(100):
            row_sum += data[i][j]
            col_sum += data[j][i]
            if i == j:
                across_sum += data[i][j]
        if