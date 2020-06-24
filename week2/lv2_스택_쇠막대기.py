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