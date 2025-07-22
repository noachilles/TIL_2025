# 파일 전체 읽기 (read)
with open('example2.txt', 'r') as file:
    content = file.read()
    print(content)

"""
First line.
Second line.
Third line.
"""

# 파일 한 줄씩 읽기 (readline)
with open('example2.txt', 'r') as file:
    line = file.readline()
    print(line)  # 'First line.\n'
    while line:
        print(line.strip())
        line = file.readline()

# 파일 모든 줄을 리스트로 읽기 (readlines)
with open('example2.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # ['First line.\n', 'Second line.\n', 'Third line.\n']
