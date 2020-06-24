def solution(n, m, image):
    from collections import deque
    answer = 0
    AREA_FIRST, SAME_AREA, NONE = 1, 0, -1
    arr = [NONE] * m * n
    
    queue = deque()
    
    for j in range(n):
        for i in range(m):
            queue.append([j,i])
            while queue:
                data = queue.popleft()
                if arr[data[0]*m+data[1]] == NONE:
                    arr[data[0]*m+data[1]] = AREA_FIRST
                #up
                if data[0] > 0:
                    if arr[(data[0]-1)*m+data[1]] == NONE and image[data[0]][data[1]]==image[data[0]-1][data[1]]:
                        arr[(data[0]-1)*m+data[1]] = SAME_AREA
                        queue.append([data[0]-1, data[1]])
                #down
                if data[0] < n-1:
                    if arr[(data[0]+1)*m+data[1]] == NONE and image[data[0]][data[1]]==image[data[0]+1][data[1]]:
                        arr[(data[0]+1)*m+data[1]] = SAME_AREA
                        queue.append([data[0]+1, data[1]])
                #left
                if data[1] > 0:
                    if arr[data[0]*m+(data[1]-1)] == NONE and image[data[0]][data[1]]==image[data[0]][data[1]-1]:
                        arr[data[0]*m+(data[1]-1)] = SAME_AREA
                        queue.append([data[0], data[1]-1])
                #right
                if data[1] < m-1:
                    if arr[data[0]*m+(data[1]+1)] == NONE and image[data[0]][data[1]]==image[data[0]][data[1]+1]:
                        arr[data[0]*m+(data[1]+1)] = SAME_AREA
                        queue.append([data[0], data[1]+1])
    
    return sum(arr)