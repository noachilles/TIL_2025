def comb(arr, n):
    result = []  # 조합을 저장할 리스트

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        
        for rest in comb(arr[i + 1:], n - 1):  # 조합
        # for rest in comb(arr[:i] + arr[i+1:], n - 1):  # 순열
        # for rest in comb(arr, n - 1):  # 중복순열
        # for rest in comb(arr[i:], n - 1):  # 중복조합
            result.append([elem] + rest)

    return result

print(comb([1, 2, 3, 4], 3))
