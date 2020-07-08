#에라토스테네스의 체 사용
'''
규칙
    1. 3개의 다른 소수의 합 = n, 3개의 서로 다른 소수는 n보다 작다.
    2. 소수의 값은 겹쳐질 수 없다.
    3. 가장 작은 3개의 소수는 2, 3, 5이기 때문에 n의 값은 최소 10이어야한다.
아이디어: 소수를 모두 찾고, 조합을 통하여 합이 n인 조합만을 골라낸다.
    1. 소수찾기: 에라토스테네스의 체를 사용 (가장 작은 두 소수의 합이 5이므로 n-4까지만 소수를 구한다.)
        1) state=[True]*(n)이 체로 사용될 예정임
        2) 2에서 n까지 반복한다.
            a. state[i]이 False일 경우 continue
            b. True일 경우 i*i부터 n-4까지 state[i배수]를 False 처리한다.
            (이때 i*i부터 하는 이유는 i보다 작은 경우 j * i로 False 처리가 되어있을 것이기 때문)
    2. 조합 후, 합이 n인 조합을 찾는다. (조합은 무작정하는 n^3방법과 combinations 사용 방법이 있음.)
복잡도: O(n^3)
'''

from itertools import combinations
def search_prime(n):
    state = [True] * (n)
    primes =[]
    for i in range(2, n):
        if state[i] == False: continue
        primes.append(i)
        for j in range(i*i, n, i):
            state[j] = False
    return primes

#combinations 사용
def solution(n):
    answer = 0
    if n < 10:
        return 0
    primes = list(combinations(search_prime(n-4),3))
    for p1, p2, p3 in primes:
        if p1 + p2 + p3 == n:
            answer += 1
    return answer 

# 3중 for문 사용
# def solution(n):
#     answer = 0
    # if n < 10:
    #     return 0
#     primes = search_prime(n-4)
#     for k in range(len(primes)):
#         for j in range(k+1, len(primes)):
#             for i in range(j+1, len(primes)):
#                 if primes[k] + primes[j] + primes[i] == n:
#                     print( primes[k], primes[j], primes[i])
#                     answer += 1
        
#     return answer