'''
규칙
    1. 전형적인 BFS문제
    2. (0,0)에서 시작해 (n, m)에 도착하는 최소 길이 구하기
    3. 도달할 방법이 없을 경우 -1, 있을 경우 최소 길이 리턴
    
로직 
    1. (0,0)을 큐에 넣고 큐가 빌 때까지 반복한다.
        1. 큐에서 팝한 위치의 앞 뒤 양옆을 비교해본다.
        2. 앞 뒤 양 옆 중 map이 1일 경우 그리고 0보다 작거나 맵보다 크지 않을 경우
            a. 팝한 위치의 값을 해당하는 위치의 맵에 더한다.
            b. 해당 위치가 n, m일 경우 그 값을 리턴하고 
            c. 아닐 경우 큐에 더한다.
    2. 반복문을 벗어날 경우, n,m을 도달하지 못했다는 의미이므로 -1을 리턴한다.  
'''
from collections import deque
DELTAS =((0, -1), (0, 1), (1, 0), (-1, 0))
def solution(maps):
    WIDTH, HEIGHT = len(maps[0]),len(maps)
    
    queue = deque()
    queue.append((0,0))
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            next_y, next_x = y + dy, x + dx
            if 0 <= next_x < WIDTH and 0 <= next_y < HEIGHT and maps[next_y][next_x] == 1: 
                maps[next_y][next_x] += maps[y][x]
                if next_y == HEIGHT - 1 and next_x == WIDTH - 1:
                    return maps[next_y][next_x]
                queue.append((next_y, next_x))
    return -1