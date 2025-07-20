numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]


# map
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

numbers1 = input().split()
print(numbers1)  # ['1,', '2,', '3']
numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]


# zip
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)


scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
for score in zip(*scores):
    print(score)
