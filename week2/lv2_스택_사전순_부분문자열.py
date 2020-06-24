def solution(sentence):
    stack = []
    
    for i in range(len(sentence)):
        while stack and ord(stack[-1]) < ord(sentence[i]):
                stack.pop()
        stack.append(sentence[i])
        
    return ''.join(stack)