a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)  # 10 2 500
    local(500)
    print(a, b, c)  # 10 2 3
enclosed()
print(a, b)  # 1 2
