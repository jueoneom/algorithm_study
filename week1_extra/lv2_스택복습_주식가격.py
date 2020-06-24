'''
로직
prices를 for문에 넣고 반복한다. (for의 i가 cur_time 역할)
    현 price가 이전 price보다 작을 경우 이전 price를 모두 pop해준다.
    pop할 때 i - price_time을 answer에 추가해준다.
    현 price를 추가한다. 추가 형태는 [i, price[i]]
'''
def solution(prices):
    answer = []
    stack = []
    
    for i in range(len(prices)):
        while stack and (stack[-1][1] > prices[i] or i == len(prices)-1):
            price_time, _ = stack.pop()
            answer.append([price_time,i - price_time])
        stack.append([i, prices[i]])
        
    answer.append([stack.pop()[0],0])
    answer.sort(key = lambda x: x[0])
    return [time for index, time in answer]