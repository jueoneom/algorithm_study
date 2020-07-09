'''
전형적인 binary search 문제임
이 사이에 있는 값중에 최적의 값을 찾는 경우가 binary search

하한과 상한이 정해져있을 때, 최대, 최소를 찾으라는 문제가 있으면 Binary search일 확률이 높다.


[Boundary]
    1. left = 1
    2. right = max(budgets)

[Search 순서]
    3. mid = (left + right) //2
    4. 각 지방에 mid를 할당했을 때 limit(M) 을 넘는지 검사한다.
        a. 넘는다 -> right를 mid - 1와 교체
        b. 안 넘는다 -> left를 mid + 1과 교체함
    
STEP 0
    budget = [110,120,140,150]
    left = 1
    right = max(budgets) = 150
    
STEP 1) 탐색과정
    1. mid 계산
        a. mid = (left + right ) // 2 = 75
    2. 각 지방에 mid를 할당했을 때 limit을 넘는지 검사하기
        a. mid를 할당할 때 필요한 예산 = 75, 75, 75, 75 = 300
        b. limit = 485
    3. 할당이 가능한가.
        a. left = mid + 1 = 75 + 1 = 76 

'''


def solution(budgets, M):
    left = 1
    right = max(budgets)

    while left <= right:
        mid = (left + right) // 2
        total_budget = sum([min(mid, budget) for budget in budgets])

        if M < total_budget:
            right = mid - 1
        elif M >= total_budget:
            left = mid + 1
    return left - 1 

    