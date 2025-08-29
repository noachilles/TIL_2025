def division_hash(key, table_size):
    """
    Division Hash Function을 사용하여 해시 값을 계산하는 함수.
    
    매개변수:
    - key: 해시할 정수형 키 값.
    - table_size: 해시 테이블의 크기 (일반적으로 소수를 사용하는 것이 좋음).
    """
    return key % table_size

def mad_hash(key, table_size, a, b, p):
    """
    MAD (Multiply-Add-Divide) 방식의 해시 함수를 사용하여 해시 값을 계산하는 함수.
    
    수식:
      h(k) = ((a * key + b) mod p) mod table_size
      
    매개변수:
    - key: 해시할 정수형 키 값.
    - table_size: 해시 테이블의 크기.
    - a: 1 이상 p-1 이하의 정수 (보조 해시에서 사용하는 상수).
    - b: 0 이상 p-1 이하의 정수 (보조 해시에서 사용하는 상수).
    - p: 키 값 범위보다 큰 소수.
    """
    return ((a * key + b) % p) % table_size

keys = [10, 20, 30, 40, 50]
table_size = 7  # 해시 테이블의 크기, 일반적으로 소수를 사용하는 것이 좋음

# MAD 방식에 사용할 상수 값들
a = 3   # 1 이상 p-1 범위 내의 임의의 값
b = 1   # 0 이상 p-1 범위 내의 임의의 값
p = 101 # 키 값 범위보다 큰 소수 (예: 101)

print("Division Hash Function 결과:")
for key in keys:
    print(f"키 {key}의 해시 값: {division_hash(key, table_size)}")

print("\nMAD(Multiply-Add-Divide) Hash Function 결과:")
for key in keys:
    print(f"키 {key}의 해시 값: {mad_hash(key, table_size, a, b, p)}")
