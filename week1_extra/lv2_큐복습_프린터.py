from collections import deque
def solution(priorities, location):
    answer = 0
    sorted_priorities = sorted(priorities, reverse = True)
    queue = deque([[p,idx] for idx, p in enumerate(priorities)])
    
    idx = 0
    while queue:
        component = queue.popleft()
        if component[0] < sorted_priorities[idx]:
            queue.append(component)
        else:
            idx += 1
            if component[1] == location:
                break
  
    
    return idx