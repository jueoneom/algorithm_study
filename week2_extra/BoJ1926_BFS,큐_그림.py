from collections import deque

def bfs(h, w):
    queue = deque()
    visited[h][w] = True
    queue.append((h, w))
    DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
    area = 1
    while queue:
        y, x = queue.popleft()
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if 0<= next_x <width and 0<= next_y < height and not visited[next_y][next_x]:
                if painting[next_y][next_x] == painting[y][x]:
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x))
                    area += 1

    return area


#입력
height, width = list(map(int, input().split(" ")))
painting = [[0]*width for _ in range(height)]
visited = [[False]*width for _ in range(height)]
for h in range(height):
    row_arr = list(map(int, input().split(" ")))
    for w, row in enumerate(row_arr):
        painting[h][w] = row

#bfs
painting_num = 0
max_painting = 0
for h in range(height):
    for w in range(width):
        if visited[h][w] or painting[h][w] == 0:
            continue
        area = bfs(h, w)
        if max_painting < area:
            max_painting = area
        painting_num += 1
            
print(painting_num)
print(max_painting)

