import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# JSON 파일 쓰기
with open('example.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)

# JSON 파일 읽기
with open('example.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
    print(type(data))  # <class 'dict'>
