import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:
            food1 = heapq.heappop(scoville)
            food2 = heapq.heappop(scoville)
            mixed = food1 + ( food2 * 2 )
            heapq.heappush( scoville, mixed )
            answer += 1
    return answer