def comb(arr, n):
   result = []
   if n == 1: # 즉, 선택할 요소의 수가 1이면
      # n이 1이라면 더 이상 조합할 요소 X
      # 각 요소 자체가 하나의 조합이 됨 -> 바로 그 값을 반환
      return [[i] for i in arr]

   # 배열의 모든 요소를 일단 순회
   for idx in range(len())

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
