import hashlib

word = '''
금일 수업시간에 작성할 스켈레톤 코드를 lectures 에 업로드 하였습니다.

수업 시작 전 미리 clone 혹은 pull 받아두시기 바랍니다.
'''
data_list = word.split()

for data in data_list:
    # 입력 데이터를 utf-8 인코딩을 통해 바이트 형식으로 변환
    data_bytes = data.encode('utf-8')
    # hashlib의 sha256 함수를 사용하여 해시 객체 생성
    hash_object = hashlib.sha256(data_bytes)
    # 해시 객체를 16진수 문자열로 변환하여 반환
    result = hash_object.hexdigest()
    print(f"입력 '{data}'의 해시 값: {result}")