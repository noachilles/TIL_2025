def generate_numbers():
    for i in range(3):
        yield i

for number in generate_numbers():
    print(number)  # 0 1 2


def reverse_generator(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse_generator('abc'):
    print(char) # c b a


# 무한 시퀀스
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

def fibonacci_generator():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2
gen = fibonacci_generator()
# 첫 10개의 피보나치 수를 출력
for _ in range(10):
    print(next(gen))  # gen.__next__()와 동일
    
print(next(gen))  # 11번째 피보나치 수
print(next(gen))  # 12번째 피보나치 수


# 대용량 데이터 처리 
def read_large_file_with_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
# 예제 파일 경로
file_path = 'large_data_file.txt'
# 제너레이터 사용하여 파일 읽기 및 처리
for line in read_large_file_with_generator(file_path):
    print(line)
