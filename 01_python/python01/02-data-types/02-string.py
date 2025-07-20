# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 


bugs = 'roaches'
counts = 13
area = 'living room'
# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll
# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'


# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!

# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split
text = 'Hello, world!'
words = text.split(',')
print(words)  # ['Hello', ' world!']

# join
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'
