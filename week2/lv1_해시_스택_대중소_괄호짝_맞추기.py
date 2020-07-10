
def solution(sentence):
    PAIRS = {"(": ")", "{": "}", "[": "]"}
    stack = []
    
    for s in sentence:
        if s in PAIRS.keys():
            stack.append(s)
        elif stack:
            top = stack.pop()
            if s != PAIRS[top]:
                return False
        else:
            return False
        
    if stack:
        return False
 
    return True


'''
규칙
    1. 닫힌 괄호가 먼저 나오면 바로 false
    2. 짝이 안맞아도 false
    3. 닫히지 않아도 false
로직
    1. 열린 괄호는 stack으로 쌓는다.
    2. sentence는 반복문
        1. 스택이 있고, 스택의 최상단과 현 괄호가 같은 종류 & 여-닫 일때 pop한다.
        2. 스택이 있는데 스택의 최상단과 괄호가 종류가 다르면 false
        3. 스택이 없고, 괄호가 닫히는 종류면 false
    3. 스택에 남아있으면 false
'''

PAIRS = {"(" : ")", "{" : "}", "[" : "]"}
def solution(sentence):
    bracket_stack = []
    for bracket in sentence:
        if bracket in PAIRS.keys():
            bracket_stack.append(bracket)
        else:
            if bracket_stack and PAIRS[bracket_stack[-1]] == bracket:
                bracket_stack.pop()
            else:
                return False
    if bracket_stack: return False
    return True
                
                