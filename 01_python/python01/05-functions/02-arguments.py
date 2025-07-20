# Positional Arguments 
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


# Default Argument Values 
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.


# Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.


# Arbitrary Argument Lists 
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')
calculate_sum(1, 2, 3)


# Arbitrary Keyword Argument Lists 
def print_info(**kwargs):
    print(kwargs)
print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)
func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')


