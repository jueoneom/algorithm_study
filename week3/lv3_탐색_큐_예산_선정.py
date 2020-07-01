from collections import deque
from math import trunc
def solution(budgets, M):
    answer = 0
    #모든 요청이 배정될 수 있는 경우
    if sum((budgets)) <= M:
        return max(budgets)
    
    #모든 요청이 배정될 수 없는 경우
    budgets = deque(sorted(budgets))
    
    per_M = (M / len(budgets))
    remained_M = M - (per_M * len(budgets))
    
    while per_M >= budgets[0]:
        while budgets:
            if budgets[0] <= per_M:
                remained_M += (per_M - budgets.popleft())
            else:
                break
        per_M += (remained_M / len(budgets))
        remained_M = 0
        
    return trunc(per_M)