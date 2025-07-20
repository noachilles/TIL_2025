my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a
# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5

my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))  # 5
print(my_list[4][-1])  # !!!
print(my_list[-1][1][0])  # w


my_list = [1, 2, 3]
my_list[0] = 100

print(my_list)  # [100, 2, 3]


# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]


# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)
print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort
my_list = [3, 2, 1]
my_list.sort()
print(my_list)  # [1, 2, 3]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [3, 2, 1]
