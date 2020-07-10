from collections import deque
from math import ceil
def solution(progresses, speeds):
    queue = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    cur_time = 0 
    answer = []
    top = -1
    
    while queue:
        finished = queue.popleft()
        if cur_time >= finished:
            answer[top] += 1
        else:
            cur_time = finished
            answer.append(1)
            top += 1
        
    
    return answer


    '''
규칙
    1. 앞에 있는 기능이 배포될 때 함께 배포된다.
    2. 배포는 하루에 한번 100인 애를 한꺼번에
    3. progress + speed가 하루의 작업 진도임
    4. 리턴은 하루에 이루어진 배포수를 리스트로
로직
    1. 남은 작업량 / speed를 구해 남은 배포일 구해서 큐에 넣기
    2. 큐에 남아있는 작업량이 없어질 때까지 반복한다.
        0. 리스트에 1을 추가한다. 
        1. 가장 앞에 있는 일자를 기준으로 작거나 같은 일자가 있으면 pop후,  리스트[-1] +=1 
    
'''
from math import ceil
from collections import deque
def solution(progresses, speeds):
    remained_days = deque([ceil((100 - progress)/speed) for progress, speed in zip(progresses, speeds)])
    answer = []
    standard_day = 0
    while remained_days:
        if remained_days[0] > standard_day:
            standard_day = remained_days.popleft()
            answer.append(1)
        else:
            remained_days.popleft()
            answer[-1] += 1
        
        
    
    return answer