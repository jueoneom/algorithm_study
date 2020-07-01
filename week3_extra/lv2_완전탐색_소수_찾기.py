from itertools import permutations
def isPrime(n):
    if n <= 1: return False
    for i in range(2, n+1):
        if i * i > n: break
        elif n % i == 0: return False
    return True


def solution(numbers):
    answer = 0
    combination = []
    for i in range(1, len(numbers)+1):
        combination += list(map( ''.join, permutations(numbers, i)))
    combination = set(map(int, combination))
    
    for comb in combination:
        if comb and isPrime(int(comb)):
            answer += 1
    
    return answer