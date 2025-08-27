def counting_sort(arr, max_value):
    n = len(arr)  # 배열의 길이
    count_arr = [0] * (max_value + 1)  # 최대값 + 1을 기준으로 임시 공간 할당
    result = [0] * n  # 정렬 결과를 저장할 변수

    # 각 요소의 빈도 계산
    for num in arr:
        count_arr[num] += 1

    # 각 숫자가 들어가야 할 인덱스를 저장하기 위해서, 누적합을 계산
    for i in range(1, max_value + 1):
        # dp와 같은 느낌으로
        # 이전까지 나온 수들의 합이 i가 놓을 수 있는 위치
        count_arr[i] += count_arr[i - 1]

    # 거꾸로 순회하면서, 현재 자신이 놓여야 하는 위치가 값을 놓고
    # 놓을 수 있는 위치를 -1 함
    for i in range(n - 1, -1, -1):
        val = arr[i]
        result[count_arr[val] - 1] = val
        count_arr[val] -= 1

    return result  # 정렬된 결과 반환

arr = [0, 4, 1, 3, 1, 2, 4, 1]
result = counting_sort(arr, 4)
print(result)  # [0, 1, 1, 1, 2, 3, 4, 4]