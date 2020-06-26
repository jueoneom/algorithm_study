#demi's code
'''
힙문제
체력이 낮은 캐가 아이템 선택 우선권을 가져야 
>> 나보다 체력이 낮은 캐가 쓸 수 있던 아이템은 나도 쓸 수 있음
범위: 전체 아이템 [ 내가 쓸 수 있는 아이템 [나보다 체력이 낮은 캐릭터가 쓸 수 있는 아이템]]
<point>
* 캐릭터는 체력이 낮은 순으로 조회
* 이이템도 체력이 낮은 순으로 조회
* 다음 캐릭터로 넘어갔을 때 이전에 검사한 아이템을 다시 검사하지 않아도 됨
'''
'''
[time complexity]
기본으로 소요되는 비용 : character, item sorting비용
    캐릭터를 체력순으로 정렬하는 비용 : O(mlogm)
    아이템을 체력순으로 정렬하는 비용 : O(nlogn)
최악의 상황에서 상정되는 비용 : 
    모든 아이템이 힙에 들어감 O(nlogn)
    모든 캐릭터에 아이템이 적용됨 O(mlogn)
전체 : mlogm + (n+m)logn

'''
from collections import deque
import heapq

def solution(healths, items):
    answer =[]
    #enumerate()함수는 인덱스를 붙여준다. *을 item 앞에 붙이면 item을 unpacking 하고 다시 packing 하게됨
    items=[(*item, idx) for idx, item in enumerate(items, 1)]
    BUFF, DEBUFF, INDEX = 0, 1, 2
    items.sort(key = lambda x: x[DEBUFF])
    items = deque(items) #items의 중복을 막기 위해서 & 

    #빈 리스트에는 heapify할 필요가 없음!!!!!! (중요!!) 
    #heapify : heap 구조로 정렬하는 함수임. 원소가 없으면 필요 없다.
    #heap 자료구조는 자료의 삽입과 삭제가 빈번하고 계속 정렬이 필요할 때 사용함
    candidates = [] #쓸 수 있는 아이템을 담는 힙
    answer = []

    for health in healths:
        while items and (health - items[0][DEBUFF] >= 100):
            item = items.popleft()
            heapq.heappush(candidates, (-item[BUFF], item[INDEX]))
        if candidates:
            answer.append(heapq.heappop(candidates)[1])
            

    return answer