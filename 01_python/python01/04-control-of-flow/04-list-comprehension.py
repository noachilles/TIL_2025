numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]


data1 = [[0] * (10) for _ in range(10)]
# 또는
data2 = [[0 for _ in range(10)] for _ in range(10)]
