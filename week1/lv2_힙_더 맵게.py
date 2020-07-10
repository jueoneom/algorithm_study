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



'''
규칙
    1. 스코빌이 낮은 두개의 음식을 섞어서 새로운 음식을 만들어 다시 넣는다.
    2. 최소 두개의 음식이 필요함 mixed = food1 + food2*2
    3. 모든 음식의 스코빌 지수를 K이상으로 만들 수 없으면 -1 리턴
    
로직
    0. 스코빌 리스트의 개수가 2개 미만이고 K에 도달하지 못하면 -1
    1. 스코빌 리스트의 개수가 2개 이상이고, 가장 작은 스코빌이 K미만일 때 반복한다. 
        0. mixed_count += 1
        1. 스코빌 리스트를 힙으로 구성하고 두개를 뽑아내서 계산한다.
        2. 그리고 다시 스코빌 리스트에 넣는다.
    
'''

import heapq
def solution(scoville, K):
    mixed_count = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        mixed = food1 + food2 * 2
        heapq.heappush(scoville, mixed)
        mixed_count += 1
    if scoville[0] < K:
        return -1
    return mixed_count
        