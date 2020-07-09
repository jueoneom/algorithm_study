'''
규칙
    1. 참여자 중에 완주하지 않은 참가자를 골라내라. 
    2. 동명이인 가능함 (set 불가능)
    3. 1개 이상 20개 이하의 알파벳 소문자임
    
로직
    1. 완주자 목록을 이름 : 동명이인 수 의 dict로 구성한다.
    2. 각 participant를 탐색하며 완주자 목록에 있는지 확인한다. 
        a. 있을 경우 -1 
        b. 없거나 0일 경우 해당 참가자 이름을 리턴한다.
복잡도: 참가자 탐색 for문 => O(n)
'''
from collections import Counter
def solution(participants, completions):
    answer = ''
    completions = dict(Counter(completions))
    
    for participant in participants:
        if not completions.get(participant, False) or completions[participant] == 0:
            return participant
        else: 
            completions[participant] -= 1
    return answer