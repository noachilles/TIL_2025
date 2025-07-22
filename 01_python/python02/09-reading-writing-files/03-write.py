# 파일 쓰기 (덮어쓰기)
with open('example3.txt', 'w') as file:
    file.write('Hello, World!\n')

# 파일 추가 쓰기
with open('example3.txt', 'a') as file:
    file.write('Appending this line.\n')

# 여러 줄 쓰기
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('example3.txt', 'a') as file:
    file.writelines(lines)
