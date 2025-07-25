import csv

# with open('users.csv', 'r', encoding='utf-8') as file:
#     # content = file.read() # 내부 텍스트가 모두 출력됨
#     # print(content)
#     csv_reader = csv.reader(file)
#     print(csv_reader) # <_csv.reader object at 0x000002B0F5EF7940>
    
#     for row in csv_reader:
#         print(row)

with open('users.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)