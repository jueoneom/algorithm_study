from collections import deque
n, k = list(map(int, input().split(" ") ))
queue = deque([i for i in range(1,n+1)])
answer = "<"
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
        
    answer += str(queue.popleft())
    answer += ", "
answer = answer[:-2] + ">"
print(answer)
    