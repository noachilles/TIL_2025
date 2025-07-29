numbers = [1, 2, 3]


def square(num):
    return num**2


new_numbers = list(map(square, numbers))
print(new_numbers)  # [1, 4, 9]
