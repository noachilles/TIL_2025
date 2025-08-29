def polynomial_hash(s, p=31, m=1000000009):
    """
    다항식 해시 함수를 사용하여 문자열의 해시 값을 계산하는 함수.
    
    이 함수는 문자열 s의 각 문자를 정수로 변환하고,
    각 문자의 위치에 따라 p의 거듭제곱을 곱하여 누적합을 구한 후,
    최종 합계를 m으로 나눈 나머지를 해시 값으로 사용한다.
    
    수식:
      h(s) = ( s[0]*p^0 + s[1]*p^1 + ... + s[n-1]*p^(n-1) ) mod m
      
    매개변수:
    - s: 해시할 문자열
    - p: 기수(base) 값, 기본값은 31 (일반적으로 소수를 사용)
    - m: 큰 소수 값, 기본값은 1000000009
    """
    hash_val = 0  # 누적 해시 값을 저장할 변수
    p_pow = 1     # p의 거듭제곱 값, 초기값은 p^0 = 1
    
    # 문자열의 각 문자에 대해 순서대로 해시 값을 계산
    for char in s:
        # 각 문자를 아스키 코드(ord)를 사용하여 정수로 변환하고,
        # 현재 위치에 해당하는 p_pow 값을 곱하여 누적합에 더함
        hash_val = (hash_val + ord(char) * p_pow) % m
        # 다음 문자를 위해 p의 거듭제곱 값을 업데이트
        p_pow = (p_pow * p) % m
        
    return hash_val

strings = ["hello", "world", "polynomial", "hash", "function"]
p = 31           # 기수 (일반적으로 소수 사용)
m = 1000000009   # 큰 소수

print("Polynomial Hash Function 결과:")
for s in strings:
    h_val = polynomial_hash(s, p, m)
    print("문자열 '{}'의 해시 값: {}".format(s, h_val))
