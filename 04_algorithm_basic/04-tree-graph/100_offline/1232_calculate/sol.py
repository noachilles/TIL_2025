import sys
sys.stdin = open('input.txt')

def postfix(idx):
    if idx <= N:
        if len(tree[idx]) == 1:
            expression.append(tree[idx][0])

        else:
            postfix(tree[idx][1])
            postfix(tree[idx][2])
            expression.append(tree[idx][0])


def calculate(expression):
    res, new = expression[0], expression[1]
    for i in range(2, len(expression)):
        if expression[i] == '+':
            res += new
        elif expression[i] == '-':
            res -= new
        elif expression[i] == '*':
            res *= new
        elif expression[i] == '/':
            res //= new
        else:
            new = expression[i]
    return res

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N):
        input_data = input().split()
        if len(input_data) == 4:
            tree[int(input_data[0])] = [input_data[1], int(input_data[2]), int(input_data[3])]
        else:
            tree[int(input_data[0])] = [int(input_data[1])]
    expression = []
    postfix(1)
    print(expression)
    print(calculate(expression))
