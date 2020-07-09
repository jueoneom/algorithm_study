
# queue를 사용한 풀이 - 효율성이나 정확성 면에서 훨씬 짧은 시간이 걸리더라구요! 
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

# 이분탐색을 사용한 풀이
'''
규칙
    1. 이분탐색으로 풀기
    2. 모든 요청의 합이 예산 M을 넘을 경우 상한액을 계산하여 배정한다.
    3. 상한액 이하는 그대로, 상한액 초과는 상한액을 배정함.
    4. 리턴값은 상한액
로직
    1. min_per_budget = 0, max_per_budget = max(budgets)을 지정한다.
    2. min_per_budget <= max_per_budget을 기준으로 반복문을 돌린다.
        1. mid = min + max //2
        2. budget을 돌면서 mid와 budget 중 min값을 골라 더하여 토탈을 구한다.
        3. total이 M보다 클경우 max = mid - 1
        4. total이 M보다 작거나 같을 경우 min = mid + 1
    3. return min - 1
        
'''

def solution(budgets, M):
    min_per_budget = 0
    max_per_budget = max(budgets)
    
    while min_per_budget <= max_per_budget:
        mid = (min_per_budget + max_per_budget) // 2
        total_budget = sum([min(mid, budget) for budget in budgets])
        if total_budget > M:
            max_per_budget = mid - 1
        elif total_budget <= M:
            min_per_budget = mid + 1
    
    
    return min_per_budget - 1