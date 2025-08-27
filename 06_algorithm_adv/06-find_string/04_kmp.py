def get_lps(pattern):
    """
    LPS(Longest Proper Prefix which is also Suffix) 배열을 계산
    패턴의 각 위치에서 접두사와 접미사가 일치하는 최대 길이를 저장
    """
    lps = [0] * len(pattern)  # LPS 배열 초기화
    j = 0  # 현재까지 일치하는 접두사의 길이
    i = 1  # 패턴의 두 번째 문자부터 시작

    while i < len(pattern):  # i가 패턴 길이 넘어서기 전까지
        # 패턴이 일치하는 경우에는,
        if pattern[j] == pattern[i]:
            #  접두-접미 일치하는 최대길이 + 1
            j += 1
            # lps 값 세팅
            lps[i] = j
            # i 도 한 칸 앞으로 전진
            i += 1

        # 패턴이 일치하지 않는 경우
        else:
            # j == 0 이라면,
            # 즉, 일치했던 게 없었던 경우는 lps[i]=0으로 하고,
            # 그냥 i를 한 칸 앞으로
            if j == 0:
                lps[i] = 0
                i += 1

            # 여태까지 일치가 발생했던 경우면
            # 이전까지 발생한 접두-접미 일치하는 최대길이만큼
            # 패턴을 땡김
            else:
                j = lps[j - 1]
    return lps


def kmp(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = get_lps(pattern)  # LPS 배열 계산

    i = 0  # 텍스트의 인덱스
    j = 0  # 패턴의 인덱스

    # 이 i랑 j는 같이 앞으로 가면서 비교
    while i < N:
        if pattern[j] == text[i]:
            # 문자가 일치하면 양쪽 인덱스를 증가
            i += 1
            j += 1

        if j == M:
            # 패턴을 완전히 찾은 경우
            print(f"패턴 {i - j}에서 발견")
            # 다음 일치를 찾기 위해 j를 LPS 배열을 이용하여 갱신
            # 이전 부분 일치 길이만큼 이동해서 다시 탐색
            j = lps[j - 1]

        # 불일치가 발생한 경우
        elif i < N and pattern[j] != text[i]:
            # 완전한 불일치인 경우, 그냥 i만 한 칸 앞으로
            if j == 0:
                i += 1
            # 이전 부분 일치 길이만큼 패턴을 땡김
            # i는 고정하고, j의 값만 되돌려놓음으로써, 사실상 패턴을 앞으로 땡기는 것과 같은 효과
            else:
                j = lps[j - 1]


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp(text, pattern)
