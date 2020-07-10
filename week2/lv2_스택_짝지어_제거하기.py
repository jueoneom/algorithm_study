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


    '''
규칙
    1. 동일 문자열이 인접해 있으면 제거한다.
    2. 모두 제거하면 1, 남아있으면 0을 반환한다.
로직
    1. 스택을 사용한다.
    2. sentence를 for문을 돌린다
    3. alphabet이 스택의 맨 위와 동일하면 팝
    4. 아니면 푸쉬
    5. 총 개수를 확인하여 반환한다.
'''
        
def solution(sentence):
    alphabet_stack = []
    for alphabet in sentence:
        if alphabet_stack and alphabet_stack[-1] == alphabet:
            alphabet_stack.pop()
        else:
            alphabet_stack.append(alphabet)
            
    if not alphabet_stack:
        return 1
    else: return 0