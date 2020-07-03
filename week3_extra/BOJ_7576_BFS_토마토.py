from collections import deque
#입력
width, height = list(map(int, input().split(" ")))
tomato_storage = [[0]*width for _ in range(height)]

#BFS
answer = 0
DELTAS =((0, 1), (0, -1), (1, 0), (-1, 0))
queue = deque()
for h in range(height):
    row_arr = list(map(int, input().split()))
    for w, row in enumerate(row_arr):
        tomato_storage[h][w] = row
        if row == 1:
            queue.append((h,w))

while queue:
    y, x = queue.popleft()
    for dy, dx in DELTAS:
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < height and 0 <= next_x < width and tomato_storage[next_y][next_x] == 0:
            tomato_storage[next_y][next_x] = tomato_storage[y][x] + 1
            if answer < tomato_storage[next_y][next_x]:
                answer = tomato_storage[next_y][next_x]
            queue.append((next_y, next_x))
for tomatoes in tomato_storage:
    if 0 in tomatoes:
        answer = -1
        break

if answer == 0 or answer == -1:
    print(answer)
else:
    print(answer - 1)

