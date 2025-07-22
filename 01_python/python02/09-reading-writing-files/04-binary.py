# 바이너리 파일 읽기
with open('sample.png', 'rb') as file:
    data = file.read()
    print(data[:20])  # 첫 20바이트 출력

# 바이너리 파일 쓰기
with open('copy_sample.png', 'wb') as file:
    file.write(data)
