def build_bad_char_heuristic(pattern):
    """나쁜 문자 휴리스틱 테이블 생성"""
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore(text, pattern):
    """나쁜 문자 휴리스틱만 사용한 보이어-무어 문자열 검색 알고리즘"""
    bad_char = build_bad_char_heuristic(pattern)
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1

        # 패턴의 오른쪽에서 왼쪽으로 비교
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            print(f"패턴이 위치 {i}에서 발견되었습니다.")
            i += 1  # 중복 패턴을 찾기 위해 한 칸만 이동
        else:
            # 나쁜 문자 휴리스틱을 사용하여 이동
            skip = j - bad_char.get(text[i + j], -1)
            i += max(1, skip)

# 테스트
text = "ABAAABCDAAABCABAAABCABAB"
pattern = "AAABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
boyer_moore(text, pattern)