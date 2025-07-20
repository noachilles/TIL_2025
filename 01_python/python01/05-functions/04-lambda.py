addition = lambda x, y: x + y

result = addition(3, 5)
print(result)  # 8


# with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)  # [1, 4, 9, 16, 25]
