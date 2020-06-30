from collections import deque
import heapq
from math import trunc

def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x: x[0])
    jobs_que = deque(jobs)
    jobs_heap = []
    cur_time = 0
    cur_job = [-1, -1]
    
    while True:
        while jobs_que and cur_time >= jobs_que[0][0]:
            time, job = jobs_que.popleft()
            heapq.heappush(jobs_heap, [job, time])
            
        if cur_job[0] <= 0:
            if cur_job[0] != -1:
                answer += (cur_time - cur_job[1])
                print(cur_time, cur_job, answer)
            if jobs_heap:
                cur_job = heapq.heappop(jobs_heap)
            else:
                cur_job = [-1, -1]
        
        if not jobs_que and not jobs_heap and cur_job[0] <= 0:
            break
        
        cur_time += 1
        if cur_job[0] >0:
            cur_job[0] -= 1
    
    
    return trunc(answer/len(jobs))