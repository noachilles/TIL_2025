def selection_sort(arr):
    n = len(arr)  # 배열의 길이

    # 맨 마지막 값은 굳이 비교할 필요가 없으므로, n-1까지만 순회
    for i in range(n - 1):
        min_idx = i  # 현재 위치를 최소값으로 가정

        # 이미 정렬된 원소 다음 위치부터 최소값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # 현재 요소가 최소값보다 작은 경우, 최소값 인덱스 갱신
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최소값과 현재 위치의 요소를 교환

arr = [64, 25, 10, 22, 11]
selection_sort(arr)
print(arr)  # [10, 11, 22, 25, 64]
