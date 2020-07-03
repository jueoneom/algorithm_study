from itertools import combinations
def isPrime(n):
    for i in range(2, n + 1):
        if i * i > n: break
        elif n % i == 0: return False
    return True


def solution(nums):
    answer = 0

    nums_comb = [n1 + n2 + n3 for n1, n2, n3 in list(combinations(nums, 3))]

    for n in nums_comb:
        if isPrime(n):
            answer += 1

    return answer