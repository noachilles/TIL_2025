# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4


# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9


# pass
for i in range(10):
    pass  # 아무 작업도 안함
