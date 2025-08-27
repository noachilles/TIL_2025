# 분할하는 부분
def quick_sort(arr, start, end):
    # start >= end 라는 건 부분 배열의 길이가 0 or 1 이라는 소리이고
    # 그렇다는 건 퀵 정렬을 진행할 필요가 없다는 소리
    if start < end:
        # 피벗을 기준으로 리스트를 분할하고 피벗의 위치를 반환 
        p = partition(arr, start, end)
        
        # 피벗을 기준으로 분할된 두 부분을 재귀적으로 정렬
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


# 분할된 영역을 정렬하는 부분
def partition(arr, start, end):
    p = arr[start]  # 피벗을 리스트의 첫 번째 요소로 설정
    left = start + 1  # 왼쪽 포인터는 피벗 다음 요소부터 시작 
    right = end  # 오른쪽 포인터는 리스트의 끝에서 시작 

    while True:
        # 왼쪽에서 피벗보다 큰 값을 찾는다
        while left <= end and arr[left] < p:
            left += 1
        # 오른쪽에서 피벗보다 작은 값을 찾는다
        while right > start and arr[right] >= p:
            right -= 1
        # 두 인덱스가 교차하지 않으면 교환
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:  # 교차하면 중단하고, 아래 로직을 실행 (31 line)
            break
    
    # 피벗과 right 인덱스의 요소를 교환 
    arr[start], arr[right] = arr[right], arr[start]
    return right  # 피벗의 최종 위치 반환 


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# 처음 인덱스를 피벗으로 설정해서 퀵 정렬 시작
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
