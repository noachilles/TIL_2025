def find_pattern(text, pattern):
    # 패턴의 길이
    M = len(pattern)
    # 전체 텍스트의 길이
    N = len(text)

    # 텍스트와 패턴을 탐색할 인덱스
    i = 0  # 텍스트 인덱스
    j = 0  # 패턴 인덱스

    # 텍스트의 끝이나 패턴의 끝에 도달할 때까지 반복
    while i < N and j < M:
        # 현재 위치의 문자가 일치하지 않는 경우
        if text[i] != pattern[j]:
            # 텍스트 인덱스를 일치 실패 지점의 다음 위치로 재설정
            i = i - j
            # 패턴 인덱스를 처음으로 재설정
            j = -1
        
        # 다음 위치로 이동
        i += 1
        j += 1

    # 패턴 전체가 일치하는지 확인
    if j == M:
        # 패턴이 시작된 텍스트의 인덱스 반환
        return i - M
    else:
        # 패턴을 찾지 못한 경우 -1 반환
        return -1

# 예제 사용
str_main = "123456789"
str_sub = "456"

# 패턴의 시작 위치 찾기
result = find_pattern(str_main, str_sub)

if result != -1:
    print(f"패턴이 텍스트의 {result}번째 위치에서 발견되었습니다.")
else:
    print("패턴을 찾을 수 없습니다.")