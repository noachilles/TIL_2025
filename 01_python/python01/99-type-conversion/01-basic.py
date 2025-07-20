# 암시적 형변환 
print(3 + 5.0)  # 8.0
print(True + 3)  # 4
print(True + False)  # 1


# 명시적 형변환 
print(int('1'))  # 1

# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))

print(int(3.5))  # 3
print(float('3.5'))  # 3.5

print(str(1) + '등')  # 1등
