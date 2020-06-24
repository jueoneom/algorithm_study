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