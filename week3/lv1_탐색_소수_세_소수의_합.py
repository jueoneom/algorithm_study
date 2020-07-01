#에라토스테네스의 채 사용
def search_prime(n):
    answer = []
    state = [True] * (n)
    
    for i in range(2, n):
        if i * i > n : break
        elif state[i] == False: continue
        for j in range(i * i, n, i):
            state[j] = False

        
    for i in range(2, len(state)):
        if state[i]: answer.append(i)
            
    return answer
            
    
def solution(n):
    answer = 0
    primes = search_prime(n)
    for k in range(len(primes)):
        for j in range(k+1, len(primes)):
            for i in range(j+1, len(primes)):
                if primes[k] + primes[j] + primes[i] == n:
                    print( primes[k], primes[j], primes[i])
                    answer += 1
        
    return answer