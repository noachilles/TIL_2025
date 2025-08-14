# 3개의 선택된 값을 저장할 리스트 초기화
selected = [0] * 3

# i, j, m은 각각 첫 번째, 두 번째, 세 번째 선택된 값을 나타냄
for i in range(2):
    selected[0] = i # 첫 번째 값 설정
    for j in range(2):
        selected[1] = j # 두 번째 값 설정
        for m in range(2):
            selected[2] = m # 세 번째 값 설정
            subset = [] # 부분 집합을 저장할 리스트 초기화
            for n in range(3): # selected 리스트의 각 요소에 대해 반복
                if selected[n] == 1: # 요소가 1인 경우 (값이 설정된 경우)
                    subset.append(n+1) # 부분 집합

            print(subset) # 현재 부분 집합 출력
