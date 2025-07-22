with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!')

with open('example.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
