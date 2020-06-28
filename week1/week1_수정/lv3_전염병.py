from collections import deque
INFEST, VACCINATED, NORMAL = 1, 0, -1
def solution(m, n, infests, vaccinateds):
    answer = 0
    visited = [NORMAL] * n * m
    
    for infest in infests:
        visited[(infest[0] - 1) * n + infest[1] - 1] = INFEST
        
    for vac in vaccinateds:
        visited[(vac[0] - 1) * n + vac[1] - 1] = VACCINATED
    
    infest_que = deque(infests)
    total_infected = m * n - len(vaccinateds)
    infested_counts = len(infests)
    
    while infested_counts < total_infected:
        if not infest_que and NORMAL in visited:
            return -1
        elif not infest_que:
            break
        
        infested_counts = bfs(m, n, infest_que, infested_counts, visited)
        answer += 1
        
    return answer


def bfs (m, n, infest_que, infested_counts, visited):
    for _ in range(len(infest_que)):
        DELTAS = ((0,1),(0,-1),(1,0),(-1,0))
        infest = infest_que.popleft()
        for dx, dy in DELTAS:
            next_y, next_x = infest[0] + dy -1, infest[1] + dx -1
            if 0 <= next_x < n and 0 <= next_y < m and visited[next_x + next_y * n] == NORMAL:
                infested_counts += 1
                visited[next_x + next_y * n] = INFEST
                infest_que.append([next_y + 1, next_x + 1])
    return infested_counts