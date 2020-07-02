def solution(sentence):
    stack = []
    
    for s in sentence:
        while stack and stack[-1] < s:
                stack.pop()
        
        stack.append(s)
        
        
    return ''.join(stack)