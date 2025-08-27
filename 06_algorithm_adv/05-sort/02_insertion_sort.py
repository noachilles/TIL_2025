def insertion_sort(arr):
    n = len(arr)  # 배열의 길이

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break


arr = [9, 5, 7, 1, 4]
insertion_sort(arr)
print(arr)  # [1, 4, 5, 7, 9]
