def solution(sentence):
    answer = 0
    stack = []
    for s in sentence:   
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s) 
        else:
            stack.append(s) 
    
    if not stack: answer = 1
    else: answer = 0
    return answer