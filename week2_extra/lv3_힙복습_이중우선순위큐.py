import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    count = 0
    
    for operation in operations:
        operation = operation.split(" ")
    
        if operation[0] == "I":
            count += 1
            num = int(operation[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif operation[1] == "1" and max_heap:
            count -= 1
            heapq.heappop(max_heap)
        elif operation[1] == "-1" and min_heap:
            count -= 1
            heapq.heappop(min_heap)
        if count <= 0:
            min_heap.clear()
            max_heap.clear()
            
    if count == 0:
        return [0,0]
    return [-max_heap[0], min_heap[0]]
    