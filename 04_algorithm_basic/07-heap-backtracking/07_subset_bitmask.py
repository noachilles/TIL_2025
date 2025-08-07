nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
n = len(nums)

for i in range(1 << n): # 모든 경우의 수에 대해서
    current_subset = []
    current_sum = 0
    for j in range(10): # j번째 요소가 선택되었는지 확인하기
        if i & (1 << j):
            current_subset.append(nums[j])
            current_sum += nums[j]
        #  --- 이까지만 있으면 1024번 다 조사---
        if current_sum > target_sum:
            break
        # 여기까지 하면 연산 횟수를 조금은 줄일 수 있으나, 큰 차이 없음
    if current_sum == target_sum:
        result.append(current_subset)

print(result)
