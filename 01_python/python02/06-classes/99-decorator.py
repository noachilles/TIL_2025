def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper


@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()
"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
