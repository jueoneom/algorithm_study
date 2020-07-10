'''
로직
레이저와 만날 때, bar가 끝날 때, bar의 개수는 하나씩 추가된다.
time complexity : O(n)
'''
from collections import deque
def solution(arrangement):
    answer = 0
    stack = deque()
    for i in range(len(arrangement)):
        if arrangement[i] == "(":
            stack.append(i)
        else:
            element = stack.pop()
            if element == i -1:
                answer += len(stack)
            else:
                answer += 1
    
    return answer


    '''
규칙
    1. ()으로 바로 닫히면 레이저고 아니면 막대기 bar임
    2. 즉 (로 생긴 막대기들이 ()에 의해 잘려서 생성되는 것. 
    3. 레이저일 경우 스택에 남아있는 ( 개수만큼 막대기 개수가 늘어나고
    4. bar가 끝나는 경우 하나의 막대기만 생성된다.
로직
    1. (이면 스택에 추가하기 
    2. )이면 레이저인지 막대기인지 확인하기 - 레이저일 경우 바로 그전 배치가 (일 것이다.
        0.공통적으로 스택에서 하나를 팝함
        1. 레이저일 경우 스택에 남아있는 ( 수만큼 더해준다.
        2. 바일 경우 1을 더해준다. 
        
'''
def solution(arrangement):
    answer = 0
    opened_bracket_count = 0
    for i, bracket in enumerate(arrangement):
        if bracket == "(":
            opened_bracket_count += 1
        else:
            opened_bracket_count -= 1
            if arrangement[i-1] == "(":
                answer += opened_bracket_count
            else:
                answer += 1
    return answer