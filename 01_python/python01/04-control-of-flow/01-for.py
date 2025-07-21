# iterable한 객체를 집어넣을 수 있음  
# 즉, 반복문에서 순회할 수 있는 객체 -> set, dict 가능  

items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)


numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)  # [8, 12, 20, -16, 10]

i = 0
numbers2 = [4, 6, 10, -8, 5]
while i < len(numbers2):
    numbers2[i] *= 2
    i += 1
print(numbers2)

elements = [['A', 'B'], ['c', 'd']]
for elem in elements:
    for item in elem:
        print(item)
