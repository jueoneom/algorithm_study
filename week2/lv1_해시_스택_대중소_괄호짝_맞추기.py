
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