import heapq

def solution(n, works):
    result = 0
    max_w = [ (-w) for w in works]
    heapq.heapify(max_w)
    
    for _ in range(n):
        work = heapq.heappop(max_w)
        if work < 0:
            work += 1
        heapq.heappush(max_w, work)
        
    return sum([work**2 for work in max_w])


'''
규칙
    1. 일의 작업량 제곱값을 최소화하도록 해야함. 가장 큰 값을 줄여야함
    2. N은 남은 시간
    3. 리턴값은 제곱해서 더한 값
로직
    1. works를 최대힙으로 구성한다.
    2. N이 0이될 때까지 지속한다. + works[0]이 0이 아닐때
        1. heappop works을 한 후 +1 하여 다시 집어넣는다.
    3. works의 각 요소를 제곱하여 더한다.
'''

import heapq
def solution(no, works):
    max_works = [-w for w in works]
    heapq.heapify(max_works)
    while no > 0 and max_works[0] < 0:
        no -= 1
        heapq.heappush(max_works, heapq.heappop(max_works) + 1)
    return sum([w * w for w in max_works])
    