a = [1, 2, 3, 4]
b = a
b[0] = 100
print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]

a = 20
b = a
b = 10
print(a)  # 20
print(b)  # 10


# 할당
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)  # [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hi'
print(original_list, copy_list)  # ['hi', 2, 3] ['hi', 2, 3]


# 얕은 복사
a = [1, 2, 3]
b = a[:]
print(a, b)  # [1, 2, 3] [1, 2, 3]
b[0] = 100
print(a, b)  # [1, 2, 3] [100, 2, 3]

# 얕은 복사의 한계 - 내부에 list가 있으면, 내부 list는 얕은 복사X  
a = [1, 2, [1, 2]]
b = a[:]
print(a, b)  # [1, 2, [1, 2]] [1, 2, [1, 2]]
b[2][0] = 100
print(a, b)  # [1, 2, [100, 2]] [1, 2, [100, 2]]



# 깊은 복사 - 얕은 복사의 한계를 극복하기 위함: 내부 리스트까지 새로운 객체를 참조하도록 함  
import copy
original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 100
print(original_list)  # [1, 2, [1, 2]]
print(deep_copied_list)  # [1, 2, [100, 2]]
