# 원소의 합이 10인 부분집합만 모두 출력하기

def find_subset(start, current_subset, current_sum):
    # 가지치기 하나 더 추가 (가지치기를 먼저 넣고 시작하지 않고, one basis rule만 먼저 설정)
    if current_sum > target_sum:
        return  # 더이상 조사의 의미가 없음

    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        # 복제본 만들기
        result.append(list(current_subset))
        # result.append(current_subset[:])
        return

    # start부터 전체 수를 다 순회
    for idx in range(start, len(nums)):
        num = nums[idx]
        # 현재 선택한 수를 집합에 넣고, 값도 추가해서 다음 작업
        current_subset.append(num)
        find_subset(idx + 1, current_subset, current_sum + num)
        current_subset.pop()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []

# 필요한 인자들은? - 어떤 인자들이 필요한지 생각
# 1. 재귀를 중단시킬 파라미터 (총합이 10이 되면 종료)
# 2. 누적해야 할 파라미터 -> 만들어지는 부분집합
# + 선택할 집합의 index 파라미터
find_subset(start=0, current_subset=[], current_sum=0)
print(result)