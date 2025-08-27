def bubble_sort(arr):
    n = len(arr)  # 배열의 길이

    for i in range(n):
        for j in range(0, n - i - 1):  # 마지막 i개 요소는 이미 정렬되어 있으므로 비교에서 제외
            if arr[j] > arr[j + 1]:  # 현재 요소가 다음 요소보다 큰 경우
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 두 요소를 교환


arr = [55, 7, 78, 12, 42]
bubble_sort(arr)
print(arr)  # [7, 12, 42, 55, 78]