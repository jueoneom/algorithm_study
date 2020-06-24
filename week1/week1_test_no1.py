from collections import deque
def solution(m, n, infests, vaccinateds):
    answer = 0
    INFEST, VACCINATED, NONE = 1, 0, -1
    arr = [NONE] *n*m
    
    for infest in infests:
        arr[(infest[0]-1)*n + infest[1]-1] = INFEST
        
    for vac in vaccinateds:
        arr[(vac[0]-1)*n + vac[1]-1]=VACCINATED

    
    infestQue = deque(infests)
    total_infected = m * n - len(vaccinateds)
    cur_infected=len(infests)
    while cur_infected < total_infected:
        if not infestQue and NONE in arr:
            return -1
        elif not infestQue:
            break
        for _ in range(len(infestQue)):
            infest = infestQue.popleft()
            #left
            if infest[1] >= 2:
                if arr[(infest[0]-1)*n+infest[1]-2] == NONE:
                    cur_infected += 1
                    arr[(infest[0]-1)*n+infest[1]-2] = INFEST
                    infestQue.append([infest[0], infest[1]-1])

            #up
            if infest[0] >= 2:
                if arr[(infest[0]-2)*n+infest[1]-1] == NONE:
                    cur_infected += 1
                    arr[(infest[0]-2)*n+infest[1]-1] = INFEST
                    infestQue.append([infest[0]-1, infest[1]])

            #down
            if infest[0] < m:
                if arr[infest[0] * n + infest[1]-1] == NONE:
                    cur_infected += 1
                    arr[infest[0] * n + infest[1]-1] = INFEST
                    infestQue.append([infest[0]+1, infest[1]])
            #right
            if infest[1] < n:
                if arr[(infest[0]-1) * n + infest[1]] == NONE:
                    cur_infected += 1
                    arr[(infest[0]-1) * n + infest[1]] = INFEST
                    infestQue.append([infest[0], infest[1]+1])

        answer += 1
        
    
    
    return answer