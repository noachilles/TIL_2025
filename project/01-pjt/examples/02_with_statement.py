# import sys
# print(sys.getdefaultencoding()) #utf-8

data = open('example.txt', 'r')
# 첫 번째 줄에 적힌 내용을 출력함 
# print(data.read())
# 파일을 열고 다 썼으면 다시 닫아줘야 함: 메모리를 생각해서
# data.close()

# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
# print(file.read()) # with문이 끝나서 파일이 닫혔기 때문에 read()를 사용할 수 없음