def rabin_karp_rolling_hash(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101  # 해시 값의 범위를 제한하기 위한 소수
    base = 256   # ASCII 문자의 범위 (0-255)

    def calculate_hash(str):
        """
        문자열의 초기 해시 값을 계산하는 함수
        ord: 아스키코드값을 구하는 내장함수
        pow: 3번째 파라미터는 제곱을 하면서 값이 너무 커지는 걸 막기 위해
        prime보다 커지지 않도록, 자체적으로 최적화를 진행하면서 계산하는 파라미터
        => 어차피 나머지값을 사용할 거기 때문에 prime 나머지 연산으로 계산되어도 상관없다.
        """
        hash_value = 0
        for i, char in enumerate(str):
            hash_value += ord(char) * pow(base, m-1-i, prime)
        return hash_value % prime

    # 패턴과 첫 윈도우의 해시 값 계산
    pattern_hash = calculate_hash(pattern)
    window_hash = calculate_hash(text[:m])

    # 최고 자리수의 값 (base^(m-1) % prime)
    # 롤링 해쉬 진행할 때, 최고 자리수만큼 빼주기 위해서 미리 구해 놓음
    highest_power = pow(base, m-1, prime)


    # 텍스트를 순회하며 패턴 검색
    # 패턴만큼의 길이는 제외하고 검색
    for i in range(n - m + 1):
        # 해시 값이 일치하는 경우, 실제 문자열 비교
        # 해시 값이 같다고, 문자열이 같은 건 아니기 때문에!
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                print(f"패턴: {i} - {i + m - 1}")

        # 해시값이 일치하지 않는 경우
        # 검사하려는 인덱스 + 패턴 길이가 아직 문자열 전체 길이보다 작은 경우에만 ( 넘치면 안되니까)
        # 다음 윈도우로 이동 (마지막 윈도우가 아닌 경우에만)
        if i < n - m:
            # 이전 윈도우의 첫 문자 제거
            window_hash = window_hash - (ord(text[i]) * highest_power) % prime
            # 윈도우를 한 칸 이동 (base를 곱함)
            # 전체적으로 base를 곱해준 효과
            window_hash = (window_hash * base) % prime
            # 새 윈도우의 마지막 문자 추가
            # 현재 i 위치에서 패턴 m만큼 더해주면, 검사하려는 부분 문자열의 마지막 문자를 추가하게 됨
            window_hash = (window_hash + ord(text[i + m])) % prime

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
rabin_karp_rolling_hash(text, pattern)