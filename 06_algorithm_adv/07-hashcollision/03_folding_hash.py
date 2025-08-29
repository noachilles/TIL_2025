def folding_hash(key, table_size, chunk_size=2):
    """
    Folding Hash Function을 사용하여 해시 값을 계산하는 함수.
    
    키를 문자열로 변환한 후, 일정 크기의 부분(chunk)으로 나누어 각 부분을 정수로 변환해서 모두 더한다.
    만약, 정수 변환이 불가능한 경우, 각 문자의 ASCII 코드 합으로 대체한다.
    전체 합을 해시 테이블 크기(table_size)로 나눈 나머지를 해시 값으로 사용
    
    매개변수:
    - key: 해시할 키 (숫자나 문자열 모두 사용 가능).
    - table_size: 해시 테이블의 크기.
    - chunk_size: 키를 나눌 부분의 크기 (예: 2자리 또는 3자리).
    
    예:
      키가 123456일 경우, chunk_size가 2이면 "12", "34", "56"으로 분할되고,
      각 부분을 정수로 변환한 후 모두 더하여 table_size로 나눈 나머지를 해시 값으로 사용한다.
    """
    key_str = str(key)
    total = 0
    # 키를 chunk_size 길이로 잘라서 순회
    for i in range(0, len(key_str), chunk_size):
        chunk = key_str[i:i+chunk_size]
        try:
            # chunk를 정수로 변환하여 합산
            total += int(chunk)
        except ValueError:
            # 변환 불가능한 경우, 각 문자의 ASCII 코드 합산
            total += sum(ord(c) for c in chunk)
    return total % table_size

keys = [123456, "987654321", "ABCDEF", 1020304050]
table_size = 7  
chunk_size = 2  # 2자리씩 나누어 폴딩

print("Folding Hash Function 결과:")
for key in keys:
    hash_value = folding_hash(key, table_size, chunk_size)
    print(f"키 {key}의 해시 값: {hash_value}")
