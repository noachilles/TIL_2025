import sys
sys.stdin = open('input.txt')

def make_postfix(expression):
    # 연산자를 담을 stack
    stack = []
    # postfix 연산식을 담을 변수
    postfix = []

    for char in expression:
        if char.isnumeric():
            postfix.append(char)
        else:
            if stack:
                postfix.append(stack.pop())
            stack.append(char)
    if stack:
        postfix.append(stack.pop())
    return postfix

def calculate(expression):
    postfix = make_postfix(expression)
    s = int(postfix[0])
    for char in postfix:
        if char.isnumeric():
            n = int(char)
        else:
            s += n
    return s

T = 10
for tc in range(1, T+1):
    N = int(input())
    expression = input()
    res = calculate(expression)
    print(f'#{tc}', end=' ')
    print(res)