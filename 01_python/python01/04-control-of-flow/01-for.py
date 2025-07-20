items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)


numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)  # [8, 12, 20, -16, 10]


elements = [['A', 'B'], ['c', 'd']]
for elem in elements:
    for item in elem:
        print(item)


