def solution(sentence):
    stack = []
    
    for s in sentence:
        while stack and stack[-1] < s:
                stack.pop()
        
        stack.append(s)
        
        
    return ''.join(stack)


'''
규칙
    1. 전체 문자열의 순서는 바뀌면 안됨
    2. 전체 문자열은 제외
    3. 가장 뒤에있는 수 구하기
로직
    1. 스택을 사용한다.
    2. 스택의 위에 있는 값보다 더 큰 수가 나올경우 스택은 그 큰수보다 커질 때까지 팝해야함.
    3. 스택의 상단 값보다 작으면 그냥 push
'''
def solution(sentence):
    alphabet_stack = []
    for alphabet in sentence:
        while alphabet_stack and alphabet_stack[-1] < alphabet:
            alphabet_stack.pop()
        alphabet_stack.append(alphabet)
    return ''.join(alphabet_stack)
    