def check_match(expression):
    # 여는 괄호들을 일단 담아둘 스택
    stack = []
    # 괄호의 짝을 매칭시킬 수 있어야
    opening_parenthesis = '({['
    closing_parenthesis = ')}]'
    # 아래와 같은 dict 형태로도 만들 수 있음
    matching_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in expression:
        # 여는 괄호 확인
        if char in matching_dict.values():
            stack.append(char)
        # 닫는 괄호 확인
        elif char in matching_dict.keys():
            # 스택에서 나와매칭되는 짝을 찾을 수 있다면, 그 괄호 제거
            # 스택이 비어있거나, 마지막 요소의 값이 내가 찾는 여는 괄호가 아니라면
            if not stack or stack[-1] != matching_dict[char]:
                return False # 실패
            stack.pop()
        # 모든 문자를 다 순회하고, 이곳에 도달했다면
    return not stack

# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)", '()(a){(b)}']
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
