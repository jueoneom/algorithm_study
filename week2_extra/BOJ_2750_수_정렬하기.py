import heapq
rotate_num = int(input())
arr = []
for _ in range(rotate_num):
    heapq.heappush(arr,int(input()))

for _ in range(rotate_num):
    print(heapq.heappop(arr))