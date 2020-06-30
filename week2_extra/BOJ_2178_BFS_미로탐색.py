
from collections import deque
#입력
height, width = list(map(int, input().split(" ")))
roads = [[0]*width for _ in range(height)]
visited = [[0]*width for _ in range(height)]
for h in range(height):
    row_arr = input()
    for w, row in enumerate(row_arr):
        roads[h][w] = int(row)

        
#BFS
queue = deque()
DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
queue.append((0, 0))
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    for dx, dy in DELTAS:
        next_x, next_y = x + dx, y + dy
        if 0<= next_x < width and 0<= next_y < height and not visited[next_y][next_x]:
            if roads[next_y][next_x] == 1:
                visited[next_y][next_x] = visited[y][x] + 1
                queue.append((next_x, next_y))
print(visited[height-1][width-1])


