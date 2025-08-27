# 나누는 파트
def merge_sort(arr):
    n = len(arr)
    
    # 배열의 길이가 1 이하인 경우, 배열을 반환
    # 더 이상 나눌 수 없는 경우
    if n <= 1:
        return arr

    mid = n // 2  # 배열을 반으로 나눌 중간 인덱스를 구함
    left_half = arr[:mid]  # 왼쪽 절반 배열
    right_half = arr[mid:]  # 오른쪽 절반 배열

    # 왼쪽 절반과 오른쪽 절반을 재귀적으로 병합 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 정렬된 두 절반을 병합
    # 더 이상 나눌 수 없는 부분까지 가면 아래 코드가 실행되고
    # 합쳐진 결과는 다시 15,16 라인에서 결과가 변수에 할당되면서
    # 재귀를 탈출하면서 결과를 구함
    return merge(left_half, right_half)


# 합치는 파트
def merge(left, right):
    result = []  # 병합된 결과를 저장할 리스트

    # 왼쪽 배열과 오른쪽 배열이 모두 비어있지 않은 동안 반복
    while left and right:
        # 왼쪽 배열의 첫 번째 요소가 오른쪽 배열의 첫 번째 요소보다 작은 경우
        if left[0] < right[0]:
            result.append(left.pop(0))  # 왼쪽 배열의 첫 번째 요소를 결과에 추가
        else:
            result.append(right.pop(0))  # 오른쪽 배열의 첫 번째 요소를 결과에 추가

    # 왼쪽 배열에 남은 요소들을 결과에 추가
    result.extend(left)
    # 오른쪽 배열에 남은 요소들을 결과에 추가
    result.extend(right)

    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
result = merge_sort(arr)
print(result)  # [2, 8, 10, 16, 22, 30, 31, 69]