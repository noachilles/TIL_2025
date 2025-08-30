def multiplication_hash(key, table_size, A):
    """
    Multiplication Hash Function을 사용하여 해시 값을 계산하는 함수.
    
    주어진 키에 상수 A를 곱하고, 소수점 이하 부분(fractional part)을 추출
    추출한 소수점 이하 값과 해시 테이블 크기(table_size)를 다시 곱한다.
    이떄 얻은 정수 부분을 해시 값으로 사용용
    
    수식:
      h(k) = floor(table_size * ((key * A) mod 1))
      
    매개변수:
    - key (int): 해시할 정수형 키 값.
    - table_size (int): 해시 테이블의 크기.
    - A (float): 0과 1 사이의 실수 상수, 기본값은 약 0.6180339887 (일반적으로 (sqrt(5)-1)/2 사용).
    """
    # 키와 상수 A의 곱에서 소수점 이하(fractional part)를 추출
    fractional_part = (key * A) % 1
    # 해시 테이블 크기와 곱하여 정수형 해시 값으로 변환
    return int(table_size * fractional_part)

keys = [10, 20, 30, 40, 50]
table_size = 7  # 해시 테이블의 크기 (일반적으로 소수 사용 권장)
A = 0.6180339887  # 곱셈 해시 함수에서 사용하는 상수 A

for key in keys:
    # 각 키에 대해 해시 값을 계산하여 출력
    hash_value = multiplication_hash(key, table_size, A)
    print(f"키 {key}의 해시 값: {hash_value}")
