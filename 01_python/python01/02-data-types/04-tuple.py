my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)


my_tuple = (1, 'a', 3, 'b', 5)
# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'


x, y = (10, 20)
print(x)  # 10
print(y)  # 20
# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
