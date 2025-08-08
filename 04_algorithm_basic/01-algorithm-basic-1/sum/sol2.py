for _ in range(10):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # 가로 합
    row_sums = [sum(x) for x in data]

    # 세로 합
    col_sums = []
    for i in range(100):
        temp = 0
        for x in data:
            temp += x[i]
        col_sums.append(temp)

    # 대각선 합
    diag_sums = []
    temp2 = 0
    temp3 = 0
    for i in range(100):
        temp2 += data[i][i]
        temp3 += data[i][99 - i]
    diag_sums.append(temp2)
    diag_sums.append(temp3)

    sums = row_sums + col_sums + diag_sums
    ans = max(sums)
    print(f"#{T} {ans}")