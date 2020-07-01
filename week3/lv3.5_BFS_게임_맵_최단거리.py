from collections import deque

def solution(maps):
    HEIGHT, WIDTH = len(maps), len(maps[0])

    visited = [[0] * WIDTH for _ in range(HEIGHT)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    DELTAS =((0, 1), (0, -1), (1, 0), (-1, 0))
    
    while queue:
        y, x = queue.popleft()
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < WIDTH and 0 <= next_y < HEIGHT and visited[next_y][next_x] == 0 and maps[next_y][next_x] == 1:
                visited[next_y][next_x] = visited[y][x] + 1
                queue.append((next_y, next_x))
    
    if visited[HEIGHT - 1][WIDTH - 1] == 0:
        return - 1
    return visited[HEIGHT - 1][WIDTH - 1]