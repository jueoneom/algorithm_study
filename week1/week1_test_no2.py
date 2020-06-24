import heapq
def solution(n, works):
    max_works = [(-w) for w in works]
    heapq.heapify(max_works)
    for _ in range(n):
        if not max_works:
            break
        work = heapq.heappop(max_works)
        if work < 0:
            work += 1
            heapq.heappush(max_works, work)
            
    return sum([ ans**2 for ans in max_works ])