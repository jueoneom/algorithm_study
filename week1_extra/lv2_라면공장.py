'''
로직
[-supplies, dates]로 재구성하여 최대힙화 한다.
예정일 k-1 과 stock이 같거나 커질때까지 반복한다.
    최대 힙에서 date < = stock 인 요소를 찾는다.
    찾으면 stock에 supply를 더해주고 요소찾는 반복문을 종료해준다. (answer += 1)
    아니면 elements에 넣어주었다가 반복문이 끝나고 다시 추가해준다.
    
'''
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    SUPPLY, DATE = 0, 1
    max_supplies = [(-supply, date) for supply, date in zip(supplies, dates)]
    heapq.heapify(max_supplies)
    while stock <= k-1:
        elements = []
        while max_supplies:
            element = heapq.heappop(max_supplies)
            if stock >= element[DATE]:
                stock -= element[SUPPLY]
                answer += 1
                break
            else:
                elements.append(element)
        for element in elements:
            heapq.heappush(max_supplies, element)
            
    return answer